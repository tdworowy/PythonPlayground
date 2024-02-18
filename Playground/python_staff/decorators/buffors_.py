import hashlib
import pickle
import time

cache = {}


def is_obsolete(entry, duration):
    return time.time() - entry['time'] > duration


def compute_key(func, args, kw):
    key = pickle.dumps((func.__name__, args, kw))
    return hashlib.sha1(key).hexdigest()


def memoize(duration=10):
    def _memoize(func):
        def __memoize(*args, **kw):
            key = compute_key(func, args, kw)

            if key in cache and not is_obsolete(cache[key], duration):
                print("Value from cache")
                return cache[key]['value']

            result = func(*args, **kw)
            cache[key] = {'value': result, 'time': time.time()}
            return result

        return __memoize

    return _memoize


if __name__ == '__main__':
    @memoize()
    def someFunc(a, b):
        return a + b


    print(someFunc(2, 2))
    print("Cache: %s" % cache)
    print(someFunc(2, 2))
    print(someFunc(3, 3))
    print("Cache: %s" % cache)
    print(someFunc(3, 3))
