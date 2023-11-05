#Create a custom class called Value that will hold a number. Then add decorators that allow addition
#(Add) and subtraction (Sub) to a number (Value). The Add and Sub decorators can accept integers
#directly, a custom Value object or other Add and Sub decorators. Add, Sub and Value all implement
#the IValue interface and can be used recursively

from abc import ABCMeta, abstractmethod

class IValue(ABCMeta):
    @abstractmethod
    def getValue(self):
        pass

#Create a custom class called Value that will hold a number
class Value(IValue):
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return str(self.number)

#The Add and Sub decorators can accept integers directly, a custom Value object or other Add and Sub decorators.
class Add(IValue):
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return (self.number)

class Sub(IValue):
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return (self.number)
    
#Decorators
@Add
def addDecorator(number):
    return number

@Sub
def subDecorator(number):
    return number


# class ClientApplication:
#     def __init__(self):
