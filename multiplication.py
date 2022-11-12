print("This is Multiplication file")

def get_multiplication(x,y):
    print(f"x == {x} , y == {y}")
    mul = x * y
    print(f"Multiplication of {x} and {y} is {mul}")
    print("-"*70)
    return mul

get_multiplication(4,5)