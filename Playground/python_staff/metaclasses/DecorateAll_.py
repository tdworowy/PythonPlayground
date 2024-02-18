from types import FunctionType


def decorate_all(decorator):
    def deco_decorator(aClass):
        for attr, attrval in aClass.__dict__.items():
            if type(attrval) is FunctionType:
                setattr(aClass,attr,decorator(attrval))
        return aClass
    return deco_decorator