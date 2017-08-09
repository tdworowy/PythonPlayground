from types import FunctionType


def decorateAll(decorator):
    def DecoDecorator(aClass):
        for attr, attrval in aClass.__dict__.items():
            if type(attrval) is FunctionType:
                setattr(aClass,attr,decorator(attrval))
        return aClass
    return DecoDecorator