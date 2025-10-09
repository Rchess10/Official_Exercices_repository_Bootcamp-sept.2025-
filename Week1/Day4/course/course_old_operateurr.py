def addoperator(x, y):
    display = x + y
    print(display)
    return display

def divideoperator(x, y):
    if y == 0:
        print("Error: division by zero")
        return None
    result = x / y
    print(result)
    return result

