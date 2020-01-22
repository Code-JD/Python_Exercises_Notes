# from functools import reduce


# def average(list):
#     total = reduce((lambda total, element: total + element), list)
#     return total / len(list)


# average = average([1, 2, 3, 4, 5, 6])

# print(average)

from functools import reduce

def get_average(list):
    total = reduce((lambda total, element: total + element), list)
    return total / len(list)


avg = get_average([1, 2, 3, 4, 5, 6])

print(avg)

