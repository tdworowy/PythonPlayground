from setuptools import setup
from setuptools.extension import Library

setup(
    name='fibonacci_my',
    ext_modules=[
        # Extension('fibonacci_my', ['fibonacci_my.exp', 'fibonacci_my.lib', 'fibonacci_my.obj']),
        Library('fibonacci_my', ['fibonacci_my.obj']),
    ]
#TODO fix, can't import
)
