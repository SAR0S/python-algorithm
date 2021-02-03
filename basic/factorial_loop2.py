def fact(num):
    factorial = 1

    if num < 0:
        print("must be positive")
    else:
        for i in range(1, num+1):
            factorial = factorial * i
            
    return factorial


if __name__ == "__main__":
    for i in range(21):
        print("%2d! = %20d"%(i, fact(i)))