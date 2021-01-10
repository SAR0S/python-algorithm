def flip_numbers(n):
    if n == 0:
        return 0
    print(n % 10, end='')
    flip_numbers(n//10)

if __name__ == "__main__":
    num_str = input("입력 : ")
    num = int(num_str)
    flip_numbers(num)