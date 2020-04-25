def detect3num(sum):
    for x in range(1, int(sum/3)):
        for y in range(x+2, int(sum/2)):
            z= sum - x - y
            if(x*x+y*y == z*z):
                #print(x**2, "+", y**2, "=", z**2, "and sum is", x + y + z)
                return(x,y,z)
                break
                    

if __name__ == "__main__":
    print(detect3num(1000))
