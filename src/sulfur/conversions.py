from collections import Mapping, Sequence

from functools import singledispatch


@singledispatch
def js_to_python(x):
    """
    Convert javascript element returned from Selenium to a python element.

    This basically is used to wrap Selenium WebElement to sulfur owns Element
    class.
    """
    return x


@singledispatch
def python_to_js(x):
    """
    Convert a Python object into something Selenium can handle.
    """
    return x


# Lists and iterables
@js_to_python.register(tuple)
@js_to_python.register(set)
@js_to_python.register(list)
def _(L):
    cls = type(L)
    return cls(js_to_python(x) for x in L)


@python_to_js.register(tuple)
@python_to_js.register(set)
@python_to_js.register(list)
def _(L):
    cls = type(L)
    return cls(python_to_js(x) for x in L)


@js_to_python.register(dict)
def _(D):
    return {k: js_to_python(v) for k, v in D.items()}


@python_to_js.register(Mapping)
def _(D):
    return {str(k): python_to_js(v) for k, v in D.items()}

#
# Conversion of python objects to javascript source
#
@singledispatch
def js_source(x):
    """
    Convert a Python object into an equivalent Javascript object. The result
    is the Javascript required to initialize the given object.
    """
    clsname = type(x).__name__
    raise TypeError('cannot convert to javascript: %r' % clsname)


@js_source.register(str)
def _(x):
    return repr(x)


@js_source.register(int)
@js_source.register(float)
def _(x):
    return str(x)


@js_source.register(bool)
def _(x):
    return str(x).lower()

@js_source.register(type(None))
def _(x):
    return 'null'


@js_source.register(Sequence)
def _(L):
    return '[%s]' % ', '.join(js_source(x) for x in L)


@js_source.register(Mapping)
def _(D):
    return '{%s}' % ', '.join('%r: %s' % (str(k), js_source(v)) for k, v in D.items())