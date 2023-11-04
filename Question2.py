#Create a custom class called Value that will hold a number. Then add decorators that allow addition
#(Add) and subtraction (Sub) to a number (Value). The Add and Sub decorators can accept integers
#directly, a custom Value object or other Add and Sub decorators. Add, Sub and Value all implement
#the IValue interface and can be used recursively

# Value class
class Value:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

# Add function
def Add(a, b):
    if isinstance(a, Value):
        a = a.value
    if isinstance(b, Value):
        b = b.value
    return Value(a + b)

# Sub function
def Sub(a, b):
    if isinstance(a, Value):
        a = a.value
    if isinstance(b, Value):
        b = b.value
    return Value(a - b)

# Client Application class
class ClientApplication:
    def __init__(self):
        value1 = Value(5)
        value2 = Value(3)

        result_add = Add(value1, value2)  # 5 + 3
        result_sub = Sub(value1, value2)  # 5 - 3

        print(f"Add result: {result_add}")
        print(f"Sub result: {result_sub}")

if __name__ == "__main__":
    client = ClientApplication()


