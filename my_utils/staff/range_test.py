def range_test(*args_check):
    def on_decorator(func):
        if not __debug__:
            return func
        else:
            def on_call(*args):
                for (ix, low, high) in args_check:
                    if args[ix] < low or args[ix] > high:
                        errmsq = 'Argument %s is not in range %s...%s ' % (ix, low, high)
                        raise TypeError(errmsq)
                return func(*args)

            return on_call

    return on_decorator


trace = True


def range_test_extend(**arg_checks):
    def on_decorator(func):
        if not __debug__:
            return func
        else:

            code = func.__code__
            allargs = code.co_varnames[:code.co_argcount]
            funcname = func.__name__

            def on_call(*pargs, **kwargs):
                positionals = list(allargs)
                positionals = positionals[:len(pargs)]

                for (argname, (low, high)) in arg_checks.items():
                    if argname in kwargs:
                        if kwargs[argname] < low or kwargs[argname] > high:
                            errmsq = '%s Argument %s is not in range %s...%s ' % (funcname, argname, low, high)
                            raise TypeError(errmsq)
                    elif argname in positionals:
                        position = positionals.index(argname)
                        if pargs[position] < low or pargs[position] > high:
                            errmsq = '%s Argument %s is not in range %s...%s ' % (funcname, argname, low, high)
                            raise TypeError(errmsq)
                    else:
                        if trace:
                            print('Argument %s has default value' % argname)
                return func(*pargs, **kwargs)

            return on_call

    return on_decorator


if __name__ == '__main__':
    @range_test([0, 1, 31], [1, 1, 12], [2, 0, 2009])
    def birthday(D, M, Y):
        print('Birthday = {0}/{1}/{2}'.format(D, M, Y))


    birthday(1, 1, 2)
    try:
        birthday(31, 13, 2009)
    except TypeError as e:
        print(e)


    @range_test_extend(age=(0, 120))
    def person(name, age):
        print('%s has %s age' % (name, age))


    person("test", 20)
    try:
        person("test2", 121)
    except TypeError as e:
        print(e)
