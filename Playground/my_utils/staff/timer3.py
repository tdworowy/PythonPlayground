import functools
import time


def timer(label=' ', trace=True):
    class Timer:
        def __init__(self, func):
            self.func = func
            self.alltime = 0

        def __call__(self, *args, **kwargs):
            start = time.process_time()
            result = self.func(*args, **kwargs)
            elapsed = time.process_time() - start
            self.alltime += elapsed
            if trace:
                format = '%s %s: %.5f, %.5f'
                values = (label, self.func.__name__, elapsed, self.alltime)
                print(format % values)
            return result

    return Timer


# dosen't work on methods


def timer2(label=' ', trace=True):
    def on_decorator(func):
        def on_call(*args, **kwargs):
            start = time.clock()
            result = func(*args, **kwargs)
            elapsed = time.clock() - start
            on_call.alltime += elapsed
            if trace:
                format = '%s %s: %.5f, %.5f'
                values = (label, func.__name__, elapsed, on_call.alltime)
                print(format % values)
            return result

        on_call.alltime += 0
        return on_call

    return on_decorator


def timer3(f):
    is_evaluating = False

    @functools.wraps(f)
    def g(*args, **kwargs):
        nonlocal is_evaluating
        if is_evaluating:
            return f(*args, **kwargs)
        else:
            start_time = time.perf_counter()
            is_evaluating = True
            try:
                value = f(*args, **kwargs)
            finally:
                is_evaluating = False
            end_time = time.perf_counter()
            print('time taken: {time}'.format(time=end_time - start_time))
            return value

    return g


@timer("==>")
def list_comp(x):
    return [x * 2 for x in range(x)]


if __name__ == "__main__":
    list_comp(10000000)
