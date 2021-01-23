a = [1] * 11
def calc_array(n):
    a[0] = 0
    i = 3
    while i <= n:
        a[i] = a[i-1] + a[i-2]
        i = i + 1

if __name__ == "__main__":
    calc_array(10)
    i = 0
    while i <= 7:
        print(a[i])
        i = i + 1