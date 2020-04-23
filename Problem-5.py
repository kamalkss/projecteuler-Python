def devideto(x):
    for i in range(1, 21):
        if(x % i != 0):
            return False
    return True


if __name__ == "__main__":
    i = 2520
    while True:
        if(devideto(i)):
            print(i)
            break       
        i += 2520
