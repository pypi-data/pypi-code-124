"""A set of common handlers to parse and route AWS service requests."""
import logging
import traceback
from functools import lru_cache
from typing import Any, Dict, Optional, Union

from botocore.model import ServiceModel

from localstack import config
from localstack.http import Response

from ..api import CommonServiceException, RequestContext, ServiceException
from ..api.core import ServiceOperation
from ..chain import ExceptionHandler, Handler, HandlerChain
from ..protocol.parser import RequestParser, create_parser
from ..protocol.serializer import create_serializer
from ..protocol.service_router import determine_aws_service_name
from ..skeleton import Skeleton, create_skeleton
from ..spec import load_service

LOG = logging.getLogger(__name__)


class ServiceNameParser(Handler):
    """
    A handler that parses heuristically from the request the AWS service the request is addressed to.
    """

    def __call__(self, chain: HandlerChain, context: RequestContext, response: Response):
        service = determine_aws_service_name(context.request)

        if not service:
            return

        context.service = self.get_service_model(service)
        headers = context.request.headers
        headers["x-localstack-tgt-api"] = service  # TODO: probably no longer needed

    @lru_cache()
    def get_service_model(self, service: str) -> ServiceModel:
        return load_service(service)


class ServiceRequestParser(Handler):
    """
    A Handler that parses the service request operation and the instance from a Request. Requires the service to
    already be resolved in the RequestContext (e.g., through a ServiceNameParser)
    """

    parsers: Dict[str, RequestParser]

    def __init__(self):
        self.parsers = dict()

    def __call__(self, chain: HandlerChain, context: RequestContext, response: Response):
        # determine service
        if not context.service:
            LOG.debug("no service set in context, skipping request parsing")
            return

        return self.parse_and_enrich(context)

    def get_parser(self, service: ServiceModel):
        name = service.service_name

        if name in self.parsers:
            return self.parsers[name]

        self.parsers[name] = create_parser(service)
        return self.parsers[name]

    def parse_and_enrich(self, context: RequestContext):
        parser = self.get_parser(context.service)
        operation, instance = parser.parse(context.request)

        # enrich context
        context.operation = operation
        context.service_request = instance


class SkeletonHandler(Handler):
    """
    Expose a Skeleton as a Handler.
    """

    def __init__(self, skeleton: Skeleton):
        self.skeleton = skeleton

    def __call__(self, chain: HandlerChain, context: RequestContext, response: Response):
        skeleton_response = self.skeleton.invoke(context)
        response.update_from(skeleton_response)


class ServiceRequestRouter(Handler):
    """
    Routes ServiceOperations to Handlers.
    """

    handlers: Dict[ServiceOperation, Handler]

    def __init__(self):
        self.handlers = dict()

    def __call__(self, chain: HandlerChain, context: RequestContext, response: Response):
        if not context.service:
            return

        service_name = context.service.service_name
        operation_name = context.operation.name

        key = ServiceOperation(service_name, operation_name)

        handler = self.handlers.get(key)
        if not handler:
            error = self.create_not_implemented_response(context)
            response.update_from(error)
            chain.stop()
            return

        handler(chain, context, response)

    def add_handler(self, key: ServiceOperation, handler: Handler):
        if key in self.handlers:
            LOG.warning("overwriting existing route for %s", key)

        self.handlers[key] = handler

    def add_provider(self, provider: Any, service: Optional[Union[str, ServiceModel]] = None):
        if not service:
            service = provider.service

        self.add_skeleton(create_skeleton(service, provider))

    def add_skeleton(self, skeleton: Skeleton):
        """
        Creates for each entry in the dispatch table of the skeleton a new route.
        """
        service = skeleton.service.service_name
        handler = SkeletonHandler(skeleton)

        for operation in skeleton.dispatch_table.keys():
            self.add_handler(ServiceOperation(service, operation), handler)

    def create_not_implemented_response(self, context):
        operation = context.operation
        service_name = operation.service_model.service_name
        operation_name = operation.name
        message = f"no handler for operation '{operation_name}' on service '{service_name}'"
        error = CommonServiceException("InternalFailure", message, status_code=501)
        serializer = create_serializer(context.service)
        return serializer.serialize_error_to_response(error, operation)


class ServiceExceptionSerializer(ExceptionHandler):
    """
    Exception handler that serializes the exception of AWS services.
    """

    handle_internal_failures: bool

    def __init__(self):
        self.handle_internal_failures = True

    def __call__(
        self,
        chain: HandlerChain,
        exception: Exception,
        context: RequestContext,
        response: Response,
    ):
        if not context.service:
            return

        error = self.create_exception_response(exception, context)
        if error:
            response.update_from(error)

    def create_exception_response(self, exception: Exception, context: RequestContext):
        operation = context.operation
        service_name = context.service.service_name
        error = exception

        if operation and isinstance(exception, NotImplementedError):
            action_name = operation.name
            message = (
                f"API action '{action_name}' for service '{service_name}' " f"not yet implemented"
            )
            LOG.info(message)
            error = CommonServiceException("InternalFailure", message, status_code=501)

        elif not isinstance(exception, ServiceException):
            if not self.handle_internal_failures:
                return

            if config.DEBUG:
                exception = "".join(
                    traceback.format_exception(
                        type(exception), value=exception, tb=exception.__traceback__
                    )
                )

            # wrap exception for serialization
            if operation:
                operation_name = operation.name
                msg = "exception while calling %s.%s: %s" % (
                    service_name,
                    operation_name,
                    exception,
                )
            else:
                # just use any operation for mocking purposes (the parser needs it to populate the default response)
                operation = context.service.operation_model(context.service.operation_names[0])
                msg = "exception while calling %s with unknown operation: %s" % (
                    service_name,
                    exception,
                )

            status_code = 501 if config.FAIL_FAST else 500

            error = CommonServiceException("InternalError", msg, status_code=status_code)

        serializer = create_serializer(context.service)  # TODO: serializer cache
        return serializer.serialize_error_to_response(error, operation)
