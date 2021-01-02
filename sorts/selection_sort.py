import random

def my_selection_sorting(data):
    for index in range(len(data) - 1):
        lowest = index
        for index2 in range(index + 1, len(data)):
            if data[lowest] > data[index2]:
                lowest = index2
        data[index], data[lowest] = data[lowest], data[index]
    return data


a = random.sample(range(100), 10)
print('a: ',a)

b = my_selection_sorting(a)
print('a: ',a)
print('b: ',b)
