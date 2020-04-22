def Reverse(digittodiagnos):
    return digittodiagnos[::-1]


def ispalindrome(main, reverse):
    return True if(main == reverse) else False


if __name__ == "__main__":
    x = 0
    palidfromelist = [[], []]
    for i in range(900, 1000):
        for j in range(900, 1000):
            x = i * j
            if(ispalindrome(Reverse(str(x)), str(x))):
                palidfromelist.append([i, j])
    maxvalue = max(palidfromelist)
    print(maxvalue[0]*maxvalue[1])
