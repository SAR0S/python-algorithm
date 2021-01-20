import random
import time

compare_counter = 0
swap_counter = 0

def bubble_sort(random_list):
    global compare_counter, swap_counter
    for start_index in range(len(random_list) - 1):  # 1부터 (마지막 요소의 인덱스)만큼 반복한다. *리스트 길이는 말그대로 요소의 개수, 마지막 요소의 인덱스 = 리스트 길이 - 1 이다. 
        for index in range(1, len(random_list) - start_index): # index 1부터 index (마지막 요소의 인덱스)까지 반복한다. (끝 숫자 포함 x)
            if random_list[index - 1] > random_list[index]: # random_list[0] 부터 비교가능
                compare_counter += 1
                temp = random_list[index - 1]
                random_list[index - 1] = random_list[index]
                random_list[index] = temp
                swap_counter += 1

if __name__ == "__main__":
    list = []
    input_n = input("정렬할 데이터의 수 : ")
    for i in range(int(input_n)):
        list.append(random.randint(1, int(input_n)))
    print("< 정렬 전 >")
    print(list)

    start_time = time.time()
    bubble_sort(list)
    running_time = time.time() - start_time
    
    print("< 정렬 후 >")
    print(list)

    print("데이터의 크기 : {}".format(int(input_n)))
    print("비교 횟수 : {}".format(compare_counter))
    print("교환 횟수 : {}".format(swap_counter))
    print("실행 시간 : {}".format(running_time))