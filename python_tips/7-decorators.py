def hi(name="Alexa"):
    def greet():
        return "Now in the greet() func"

    def welcome():
        return "now in the welcome() func"

    return greet if name == "Henry" else welcome


a = hi()
print(a)
print(a())


def x_action():
    return "x_action"


def doSthBeforeX(func):
    print("I am do some boring work before excute x()")
    print(func())


doSthBeforeX(x_action)

# First decorator
from functools import wraps


def a_new_decorator(a_func):
    @wraps(a_func)
    def wrapTheFunc():
        print("I am doing some boring work before executing a_func()")
        a_func()
        print("I am doing some boring work after executing a_func()")

    return wrapTheFunc


@a_new_decorator
def a_function_requiring_decoration():
    """Hey you! Decorate me!"""
    print("I am the function which needs some decoration to remove my foul smell")


# the @a_new_decorator is just a short way of saying:
# a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)

a_function_requiring_decoration()

print(a_function_requiring_decoration.__name__)


# USE_CASES: Logging
def logit(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print(func.__name__ + " was called")
        return func(*args, **kwargs)

    return with_logging


@logit
def addition_func(x):
    return x + x


result = addition_func(4)


# Decorators with Arguments
def logit2(logfile="out.log"):
    def logging_decorator(func):
        @wraps(func)
        def wrapped_func(*args, **kwargs):
            log_str = func.__name__ + " was called"
            print(log_str)

            # Open the logfile and append
            with open(logfile, 'a') as opened_file:
                opened_file.write(log_str + '\n')
            return func(*args, **kwargs)

        return wrapped_func

    return logging_decorator


@logit2()
def myfunc1():
    pass


myfunc1()


@logit2(logfile='func2.log')
def myfunc2():
    pass


myfunc2()

from logit3 import logit3

logit3._logfile = 'out3.log'  # if change log file


@logit3
def myfunc3():
    pass


myfunc3()
