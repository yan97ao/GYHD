import time
import random

def quickSort1(to_sort):
    if to_sort == []:
        return []

    bigList = []
    smallList = []
    middle = to_sort[0]
    for i in to_sort[1:]:
        if i<=middle:
            smallList.append(i)
        else:
            bigList.append(i)
    return quickSort1(smallList) + [middle] + quickSort1(bigList)

def quickSort2(to_sort, begin=0, end=None):
    if end is None:
        end = len(to_sort) - 1
    if begin >= end:
        return
    def partition(to_sort, begin, end):
        pivot = begin
        for i in xrange(begin + 1, end + 1):
            if to_sort[i] <= to_sort[begin]:
                pivot += 1
                to_sort[i],to_sort[pivot] = to_sort[pivot],to_sort[i]
        to_sort[pivot],to_sort[begin] = to_sort[begin],to_sort[pivot]
        return pivot
    pivot = partition(to_sort, begin, end)
    quickSort2(to_sort, begin, pivot - 1)
    quickSort2(to_sort, pivot + 1, end)
    return to_sort

def quickSort3(to_sort):
    to_sort.sort()
    return to_sort

def test(func, test_data):
    t0 = time.time()
    print func(test_data[:])
    for i in xrange(9999):
        func(test_data[:])
    t1 = time.time()
    print "run 10000 tims %s cost %s" % (func.__name__,t1 - t0)

func_list = [quickSort1, quickSort2, quickSort3]
test_data = []
for i in xrange(100):
    test_data.append(random.randint(0,10000))
for i in func_list:
    test(i, test_data)
