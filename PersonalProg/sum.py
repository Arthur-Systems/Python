
import math


def search3(array: list, target: int or float) -> int:  # type:ignore
    left = 0
    right = len(array) - 1  # bug 3
    while left <= right:  # bug 1
        middle = math.ceil((left + right) / 2)
        print(f"left: {left}, right: {right} middle: {middle}")
        if array[middle] == target:
            return middle
        elif array[middle] < target:
            left = middle + 1
        else:
            right = middle - 1  # bug 2
    return -1  # cannot find it


def search(array: list, left: int, right: int, target: int or float) -> int:  # type:ignore
    while left <= right:  # bug 1
        middle = int((left+right)/2)
        print(f"left: {left}, right: {right} middle: {middle}")
        if array[middle] == target:
            return middle
        elif array[middle] < target:
            left = middle + 1
        else:
            right = middle - 1  # bug 2
    return -1  # cannot find it


def ifsum(array, target):
    right = len(array) - 1
    for i in range(len(array)):
        # array.remove(i)
        sub = target - array[i]
        index = search(array, i+1, right, sub)
        if index != -1:
            print(f"{array[i]} + {array[index]} = {target}")
            return True
    return False


# def ifsum2(array, target):
#     for i in array:
#         array.remove(i)
#         print(array)
#         if search(array, target - i) != -1:
#             print(f"{i} + {target - i} = {target}")
#             return True
#     return False


if __name__ == '__main__':

    # array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 4, 3, 2, 4, 5, 6, 20]
    target = 22
    print(ifsum(array, target))
    print(array)
