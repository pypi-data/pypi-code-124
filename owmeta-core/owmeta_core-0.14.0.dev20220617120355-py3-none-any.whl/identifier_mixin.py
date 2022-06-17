from __future__ import print_function
import hashlib

from rdflib.term import URIRef
from urllib.parse import quote
from six import string_types

from .graph_object import IdentifierMissingException


__all__ = ['IdMixin']


# This was pulled out of DataObject when it was used by multiple classes. It may prove
# useful for making custom GraphObjects, so it's retained here as a mixin


class IdMixin:
    '''
    Mixin that provides common identifier logic

    Attributes
    ----------
    hashfun : function
        The function to use for encoding data provided to make_identifier.
        Should return an object can ``.encode()`` to a :py:class:`bytes` (a.k.a.
        :py:class:`str` in Python 2).  Defaults to :py:func:`hashlib.sha224`
    rdf_namespace : rdflib.namespace.Namespace
        The namespace for identifiers created
    direct_key : bool
        Whether to make a key directly, just adding the string onto the namespace or
        indirectly by hashing the key before joining with the namespace.
    '''
    hashfun = hashlib.sha224

    direct_key = True

    def __init__(self, ident=None, key=None, *args, direct_key=None, **kwargs):
        super(IdMixin, self).__init__(*args, **kwargs)
        if key is not None and ident is not None:
            raise Exception("Only one of 'key' or 'ident' can be given to Context")

        if ident is not None:
            self._id = URIRef(ident)
        else:
            self._id = None

        if direct_key is not None:
            self.direct_key = bool(direct_key)

        self.key = key
        self._id_key = None
        self._generated_id = None

    @classmethod
    def make_identifier(cls, data):
        '''
        Makes an identifier based on this class' `rdf_namespace` by calling
        `__str__` on the data and passing to the class' `hashfun`.

        If the `__str__` for data's type doesn't function as an identifier, you
        should use either :meth:`make_identifier_direct` or override
        :meth:`identifier_augment` and :meth:`defined_augment`
        '''
        strdata = str(data)
        if strdata:
            hsh = "a" + cls.hashfun(strdata.encode()).hexdigest()
            return URIRef(cls.rdf_namespace[hsh])
        else:
            raise ValueError('Cannot use falsy value'
                             ' {} to make an identifier'.format(strdata))

    @classmethod
    def make_identifier_direct(cls, string):
        '''
        Make identifier by using the `~urllib.parse.quote`'d value of `key` appended to
        the `rdf_namespace` value
        '''
        if not isinstance(string, string_types):
            raise ValueError('make_identifier_direct only accepts strings')
        return URIRef(cls.rdf_namespace[quote(string)])

    def _gen_identifier(self):
        key = self.key
        if key is None:
            return None

        if key == self._id_key:
            return self._generated_id

        if self.direct_key:
            self._generated_id = self.make_identifier_direct(key)
        else:
            self._generated_id = self.make_identifier(key)
        self._id_key = key

        return self._generated_id

    @property
    def identifier(self):
        '''
        The identifier
        '''
        if self._id is not None:
            return self._id
        else:
            ident = self._gen_identifier()
            if ident is not None:
                return ident
            elif self.defined_augment():
                return self.identifier_augment()
            else:
                raise IdentifierMissingException(self)

    @identifier.setter
    def identifier(self, value):
        self._id = value

    def identifier_augment(self):
        """
        Override this method to define an identifier in lieu of one explicity set.

        One must also override :meth:`defined_augment` to return True whenever
        this method could return a valid identifier.
        :exc:`~.graph_object.IdentifierMissingException` should be
        raised if an identifier cannot be generated by this method.

        Raises
        ------
        `~.graph_object.IdentifierMissingException`

        """
        raise IdentifierMissingException(self)

    @property
    def defined(self):
        if self._id is not None or self.key is not None:
            return True
        else:
            return self.defined_augment()

    def defined_augment(self):
        """ This fuction must return False if :meth:`identifier_augment` would
        raise an :exc:`~.graph_object.IdentifierMissingException`. Override
        it when defining a non-standard identifier for subclasses of DataObjects.
        """
        return False
