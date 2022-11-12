# print("This is addition file")

def get_addition(a,b):
    print(f"a == {a} , b == {b}")
    add = a + b
    print(f"Addition of {a} and {b} is {add}")
    print("*"*70)
    return add

print('Value in __Name__ variable for addition file is :',__name__)

if __name__ == "__main__":
    get_addition(2,3)
