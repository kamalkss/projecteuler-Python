def primelist(todigit):
    return True if all(todigit % i != 0 for i in range(2, int(todigit**(1/2)+1))) else False


if __name__ == "__main__":
    counter = 2
    primelists = []
    while(True):
        if primelist(counter):
            primelists.append(counter)
            if(len(primelists) == 10001):
                print(primelists[-1])
                break
        counter += 1
