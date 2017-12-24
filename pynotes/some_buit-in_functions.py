# Fangyu
# Some built-in functions in Pyhton

# isinstance
# judge whether an object belongs to a class
# isinstance(object, _class_)

# _class_ means eg.tuple,dict,int,float

class objA:
    pass

A = objA()
B = 'a','v'
C = 'a string'

print (isinstance(A, objA))
print (isinstance(B, tuple))
print (isinstance(C, str))
# output:
# True
# True
# True


# hasattr
# The arguments are an object and a string.
# The result is True if the string is the name of one of the object’s attributes, False if not.
# (This is implemented by calling getattr(object, name) and seeing whether it raises an exception or not.)


# callable
# return True is if an object is callable
# return False if an object isn't callable


# 12/5/2016

# enumerate
# return both index and value
layers = ('conv1_1', 'relu1_1', 'conv1_2', 'relu1_2', 'pool1')
for a,b in enumerate(layers):
    print(a,b)


# 12/11/2016

# zip
a=[1,2,3]
b=[4,5,6]
ab=[a,b]
# return [(1,4),(2,5),(3,6)]
