
import time



def bubble(array,N):  # 1
    t1 = time.perf_counter()
    for i in range(N-1):
        for j in range(N-i-1):
            if array[j] > array[j+1]:
                buff = array[j]
                array[j] = array[j+1]
                array[j+1] = buff

    t2 = time.perf_counter()
    return t2 - t1




def insertion(array):   # 2
    t1 = time.perf_counter()
    for i in range(1, len(array)):
        temp = array[i]
        j = i - 1
        while (j >= 0 and temp < array[j]):
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = temp
    t2 = time.perf_counter()
    return t2 - t1


def quick (array):   # 6
    if len(array) <= 1:
        return array

    elem = array[len(array) - len(array) // 2]
    left = list(filter(lambda x: x<elem, array))
    center = [i for i in array if i == elem]
    right = list(filter(lambda x: x > elem, array))

    return  quick(left) + center + quick(right)


def check(array) :
    for i in range(1, len(array)):
        if array[i - 1] > array[i]:
            return False
    return True