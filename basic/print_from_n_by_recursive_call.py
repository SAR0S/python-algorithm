def print_from_n(n):
    print(n)
    if n > 1 :
        print_from_n(n - 1)

if __name__ == "__main__":
    print_from_n(10)