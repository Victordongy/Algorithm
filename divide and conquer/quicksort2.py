## pick the first element as the pivot
def quick_sort_first(lis):
    if len(lis) == 0:
        return 0
    elif len(lis) == 1:
        return 0
    elif len(lis) == 2:
        return 1
    else:
        pivot = lis[0]
        i = 0
        j = 1
        for index in range(1, len(lis)):
            if lis[index] < pivot:
                if i == j:
                    i = i + 1
                    j = j + 1
                else:
                    temp = lis[index]
                    lis[index] = lis[i + 1]
                    lis[i + 1] = temp
                    i = i + 1
                    j = j + 1
            else:
                j = j + 1
        temp = lis[i]
        lis[i] = lis[0]
        lis[0] = temp
        return len(lis) - 1 + quick_sort_first(lis[:i]) + quick_sort_first(lis[i + 1:])


## pick the last element as the pivot
def quick_sort_last(lis):
    if len(lis) == 0:
        return 0
    elif len(lis) == 1:
        return 0
    elif len(lis) == 2:
        return 1
    else:
        temp = lis[-1]
        lis[-1] = lis[0]
        lis[0] = temp

        pivot = lis[0]
        temp
        i = 0
        j = 1
        for index in range(1, len(lis)):
            if lis[index] < pivot:
                if i == j:
                    i = i + 1
                    j = j + 1
                else:
                    temp = lis[index]
                    lis[index] = lis[i + 1]
                    lis[i + 1] = temp
                    i = i + 1
                    j = j + 1
            else:
                j = j + 1

        temp = lis[i]
        lis[i] = lis[0]
        lis[0] = temp

        return len(lis) - 1 + quick_sort_last(lis[:i]) + quick_sort_last(lis[i + 1:])


import math
import statistics


## pick the median element as the pivot
def quick_sort_median(lis):
    if len(lis) == 0:
        return 0
    elif len(lis) == 1:
        return 0
    elif len(lis) == 2:
        return 1
    else:
        median = math.floor((len(lis) - 1) / 2)
        comparelis = [lis[0], lis[median], lis[-1]]
        if lis[0] == statistics.median(comparelis):
            index = 0
        elif lis[-1] == statistics.median(comparelis):
            index = -1
        else:
            index = median
        # print("choose ",lis[index]," from ",lis[0],lis[median],lis[-1])

        temp = lis[index]
        lis[index] = lis[0]
        lis[0] = temp

        pivot = lis[0]
        temp
        i = 0
        j = 1
        for index in range(1, len(lis)):
            if lis[index] < pivot:
                if i == j:
                    i = i + 1
                    j = j + 1
                else:
                    temp = lis[index]
                    lis[index] = lis[i + 1]
                    lis[i + 1] = temp
                    i = i + 1
                    j = j + 1
            else:
                j = j + 1

        temp = lis[i]
        lis[i] = lis[0]
        lis[0] = temp

        return len(lis) - 1 + quick_sort_median(lis[:i]) + quick_sort_median(lis[i + 1:])


lis = [1, 23, 65, 4, 654, 8, 4]
print(len(lis))
# print(quick_sort_first(lis))
# print(quick_sort_last(lis))
print(quick_sort_median(lis))