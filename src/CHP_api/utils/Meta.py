from weakref import WeakValueDictionary

from .decorators import classproperty


class SmartClientSingleton(type):
    """
    Metaclass for creating a singleton pattern that depends on the "token" parameter
    """
    _alive_tokens_: WeakValueDictionary = WeakValueDictionary()

    def __new__(mcs, name, bases, attrs):

        # add class property 'who' that return list of 'tokens' of alive objects
        attrs['who'] = classproperty(lambda cls: list(cls._alive_tokens_.keys()))

        return type.__new__(mcs, name, bases, attrs)

    def __call__(cls, *args, **kwargs):

        try:
            token_p = kwargs['token']
        except KeyError:
            raise TypeError('__init__() missing required key-value argument: \'token\'')

        if token_p not in SmartClientSingleton._alive_tokens_.keys():
            it = object.__new__(cls)
            it.__init__(*args, **kwargs)
            SmartClientSingleton._alive_tokens_[token_p] = it

        return SmartClientSingleton._alive_tokens_[token_p]
