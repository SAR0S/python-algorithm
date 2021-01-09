def check_multiple_of_3_and_5(n):
    i = 1
    while i <= n:
        if (i % 3 == 0) and (i % 5 == 0):
            print("%d"%(i))
        i = i + 1

if __name__ == "__main__":
    check_multiple_of_3_and_5(100)