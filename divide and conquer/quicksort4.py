def choose_pivot_first(lst):
    return 0

def choose_pivot_last(lst):
    return -1

def choose_pivot_random(lst):
    #random pivots
    from random import randrange
    return randrange(0, stop=len(lst))

def choose_pivot_median(lst):
    if len(lst) % 2 == 0:
        mid_index = len(lst) / 2 - 1
    else:
        mid_index = len(lst) / 2
    tmp_lst = sorted([lst[0], lst[mid_index], lst[-1]])
    return lst.index(tmp_lst[1])

def partition(lst, pivot):
    if lst[0] != lst[pivot]:
        lst[0], lst[pivot] = lst[pivot], lst[0]
    i = 1
    for j in range(1, len(lst)):
        if lst[j] < lst[0]:
            lst[i], lst[j] = lst[j], lst[i]
            i += 1
    lst[0], lst[i-1] = lst[i-1], lst[0]
    return lst[:i-1], lst[i:]

def quick_sort(lst, choose_pivot_func):
    num_comparison = len(lst) - 1
    if len(lst) <= 1:
        return lst, 0
    pivot = choose_pivot_func(lst)
    p_val = lst[pivot]
    less_part, greater_part = partition(lst, pivot)
    result1 = quick_sort(less_part, choose_pivot_func)
    result2 = quick_sort(greater_part, choose_pivot_func)
    return result1[0] + [p_val] + result2[0], num_comparison + result1[1] + result2[1]

inp_lst = open("week3/QuickSort.txt").read().split("\n")[:-1]
inp_lst = map(lambda num: int(num.strip()), inp_lst)
print "number of elements:", len(inp_lst)
print "choose_pivot_first:",  quick_sort(inp_lst, choose_pivot_first)[1]
print "choose_pivot_last:",  quick_sort(inp_lst, choose_pivot_last)[1]
print "choose_pivot_median:",  quick_sort(inp_lst, choose_pivot_median)[1]