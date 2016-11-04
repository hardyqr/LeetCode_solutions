# Fangyu
# 11/4/2016

# It is used in the data type of class.
# Whenever an object is built within the class,  __init__ would run at the very first place.
# It helps you do some initializations of the newly built object.

class Person(object):
    def __init__(self, name):
        self.name = name
    def sayHi(self):
        print( 'Hello, I am a bad '+self.name+'.')

p = Person('Mother Fucker')
p.sayHi()

# This short example can also be written as Person(Swaroop).sayHi()


'''
这里，我们把__init__方法定义为取一个参数name（以及default存在的参数self)
在这个__init__里，我们只是创建一个新的域，也称为name
注意它们是两个不同的变量，尽管它们有相同的名字。点号使我们能够区分它们

最重要的是，我们没有专门调用__init__方法
只是在创建一个类的新实例的时候，把参数包括在圆括号内跟在类名后面
从而传递给__init__方法。这是这种方法的重要之处

现在，我们能够在我们的方法中使用self.name域。这在sayHi方法中得到了验证
给C /Java/C#程序员的注释__init__方法类似于C 、C#和Java中的 constructor
'''
