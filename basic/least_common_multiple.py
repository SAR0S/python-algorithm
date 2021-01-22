def calc_LCM(a, b, c):
    i = 2
    while i <= a * b * c:
        if (i % a == 0) and (i % b == 0) and (i % c == 0):
            break 
        i = i + 1
    print("{}, {}, {}의 최소공배수 : {}".format(a, b, c, i))


if __name__ == "__main__":
    a, b, c = map(int, input("세 가지 숫자 a b c 입력> ").split())
    calc_LCM(a, b, c)