#runtime 32s
number = int(input("write number: "))

def checkpalindrome(x: int):
    n=str(x)
    return x == x[::-1]


checkpalindrome(number)
