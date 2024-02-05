number = int(input("write number: "))

def checkpalindrome(x: int):
    checkflag = True
    x = str(number)
    for i in range(0, len(x)//2):
        if x[i] != x[len(x)-1-i]:
            checkflag = False
            break  # Exit the loop if a mismatch is found

    if checkflag:
        return True
    else:
        return False

checkpalindrome(number)
