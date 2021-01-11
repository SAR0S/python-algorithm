def solve(n):
    i = 1
    while i <= n:
        if i % 3 == 0:
            print("X")
        else:
            print(i)
        i = i + 1

if __name__ == "__main__":
    solve(30)