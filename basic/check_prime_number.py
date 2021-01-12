def check_prime_number(n):
    i = 2
    while i < n:
        if n % i == 0:
            break
        i = i + 1
    if i == n:
        print("{0}는 소수\n".format(n))
    else:
        print("{0}는 합성수\n".format(n))

if __name__ == "__main__":
    check_prime_number(19)
    check_prime_number(130)
    check_prime_number(37)
    check_prime_number(20)
    check_prime_number(21)