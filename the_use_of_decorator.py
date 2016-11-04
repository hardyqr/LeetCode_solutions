# Fangyu
# 11/4/2016
# The use of decorator '@'


# This is a basic example about how we use a decorator
def hello(f):
    def wrapper():
        print ("hello, %s" % f.__name__)
        f()
        print ("goodby, %s" % f.__name__)
    return wrapper
# This is a decorator function and f is a function which you intend to use after the decorator

@hello
def foo():
    print ("i am foo")

foo()

# Here is another eg.
# What if we want to use parameters in the function 'f'?
# This link talks about how we use '*args' and'**kwargs' in a function whose parameters are not yet settled
# http://stackoverflow.com/questions/3394835/args-and-kwargs
def draw_line(f):
    def fuck(*args):
        print('----------')
        f(*args)
    return fuck

@draw_line
def func_1(x):
    print(x+'is bad')

@draw_line
def func_2(x):
    print(x+'is a motherfucker')

func_1('Trump')
func_2('Hillary')

# Using a decorator is equivalent to using a nested function
draw_line(func_2('Hillary'))
# The decorator acts as the outside layer
