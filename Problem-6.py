def sumofthesquares(x):
    sum = 0
    for i in range(1, x+1):
        sum += i**2
    return int(sum)
    
def squareofthesum(x):
    sum = 0
    for i in range(1, x+1):
        sum += i
    return int(sum**2)


if __name__ == "__main__":
    num = int(input())
    sumofthesquaresx = sumofthesquares(num)
    squareofthesumx = squareofthesum(num)
    diff =  squareofthesumx - sumofthesquaresx
    print("diff is :{0}".format(diff))
