def bubble_sort(li):
    length = len(li) - 1
    for i in range(length):
        for j in range(length-i):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]

if __name__ == "__main__":
    li = [10,2,3,4,1,7,0]
    bubble_sort(li)
    print(li)
