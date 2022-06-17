import logging
from queue import Queue, Empty
from logging.handlers import QueueHandler, QueueListener


class AsyncHandlerWrapper(QueueHandler):
    """A handler which blocks too long on handling events can be wrapped by this handler
    which will queue the logging event and redirect it to the original handler
    in a separate thread.
    """

    def __init__(self, handler: logging.Handler):
        queue = Queue()
        self._listener = QueueListener(queue, handler, respect_handler_level=True)
        self._listener.start()
        super().__init__(queue)

    @property
    def wrapped_handler(self) -> logging.Handler:
        return self._listener.handlers[0]

    def flush(self):
        """Dequeue and handle records in the current thread"""
        # Called by logging.shutdown: atexit callback
        self.acquire()
        try:
            while True:
                try:
                    record = self._listener.dequeue(block=False)
                except Empty:
                    return
                self._listener.handle(record)
        finally:
            self.release()

    def close(self):
        """Stop accepting events, process queued events and stop the listener thread."""
        # Called by logging.shutdown: atexit callback
        super().close()  # stop accepting events
        self._listener.stop()  # process the queue and stop listening
