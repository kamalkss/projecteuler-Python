def primefactor(digittodiagnos):
    return True if all(digittodiagnos%i!=0 for i in range(2,int(digittodiagnos**(1/2)+1))) else False

def primelist(todigit):
    primelists = []
    result = 1
    for i in range(2,int(todigit**(1/2))):
        if(primefactor(i) and todigit%i ==0):
            primelists.append(i)
           

    maxnumber = max(primelists)
    return maxnumber

if __name__ == "__main__":
    x = int(input())
    print(primelist(x))
    
