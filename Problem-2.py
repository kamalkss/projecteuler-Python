def iseven(digittodiagnos):
    return True if digittodiagnos % 2 ==0 else False

def fib(maxValue):
    FirstDigit = 1
    Seconddigit = 2
    sum = 2
    while(True):
        NextValue = FirstDigit + Seconddigit
        FirstDigit = Seconddigit
        Seconddigit = NextValue
        if(NextValue > maxValue):
            break
        if iseven(Seconddigit):
            sum += Seconddigit
    return sum

if __name__ == '__main__':
    x = int(input())
    print(fib(x))
