def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

def get_operation(choice):
    operations = {
        "1": add,
        "2": subtract,
        "3": multiply,
        "4": divide
    }
    return operations.get(choice)
