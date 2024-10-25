def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def divide(x, y):
    return x/y

def multiply(x, y):
    return x * y

def mod(x, y):
    return x % y

def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x-1)

if __name__ == "__main__":
    print("Executing this standalone code")
    test_divide = divide(8,4)
    print("Test divide:", test_divide)
    test_multiply = multiply(10,2)
    print("Test multiply:", test_multiply)
    test_mod = mod(6,2)
    print("Test mod:", test_mod)
