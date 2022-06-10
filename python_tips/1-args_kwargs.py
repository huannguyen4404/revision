def test_var_args(f_args, *argv):
    print("First normal arg:", f_args)
    for arg in argv:
        print("Another args through *argv:", arg)


# test_var_args('yasoob', 'python', 'eggs', 'test')

def test_var_kwargs(**kwargs):
    for key, value in kwargs.items():
        print("{0} = {1}".format(key, value))


def some_func(fargs, *args, **kwargs):
    print("First normal arg:", fargs)
    for arg in args:
        print("Another args through *argv:", arg)

    for key, value in kwargs.items():
        print("{0} = {1}".format(key, value))


def test_args_call(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)


# test_var_kwargs(name="Python", service="Revision")
# some_func(10, "the huan", "nguyen", "thiet khong", sol=7, justatee="rapper")
test_args_call("one", 2, "bar")
my_args = ("four", 5, "sheet")
test_args_call(*my_args)
my_kwargs = {"arg3": "CR7", "arg2": 222, "arg1": "111"}
test_args_call(**my_kwargs)
