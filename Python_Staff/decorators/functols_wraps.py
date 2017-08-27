from functools import  wraps

def preserving_decorator(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        """Doc in decorator"""
        return func(*args,**kwargs)
    return wrapper


def NOT_preserving_decorator(func):
    def wrapper(*args,**kwargs):
        """Docstring in decorator"""
        return func(*args,**kwargs)
    return wrapper


@preserving_decorator
def function_with_docstring():
    """Important documentation"""
@NOT_preserving_decorator
def function_with_docstring2():
    """Important documentation"""


print(function_with_docstring.__name__)
print(function_with_docstring.__doc__)
print("_"*20)
print(function_with_docstring2.__name__)
print(function_with_docstring2.__doc__)