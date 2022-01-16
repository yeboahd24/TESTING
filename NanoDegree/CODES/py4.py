# Some languages, like Java, allow you to mark a class as final that
# means you can't inherit from it. There is how it can be implemented
# in a few lines of code.


def _init_subclass(cls, *args, **kwargs) -> None:
    raise TypeError('no subclassing!')

def final(cls):
    setattr(cls, '__init_subclass__', classmethod(_init_subclass))
    return cls

@final
class A:
    pass

class B(A):
    pass
# TypeError: no subclassing!

# In python 3.8, PEP-591 (https://www.python.org/dev/peps/pep-0591/) 
# introduced typing.final (https://docs.python.org/3/library/typing.html#typing.final).
# It doesn't make a runtime check but is processed by mypy at static type checking instead.