
import math


def search2(array: list, target: int or float) -> int:  # type:ignore
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


def search(array: list, target: int or float) -> int:  # type:ignore
    left = 0
    right = len(array)  # bug 3
    while left < right:  # bug 1
        middle = int((left + right) / 2)  # important
        print(f"left: {left}, right: {right} middle: {middle}")
        if array[middle] == target:
            return middle
        elif array[middle] < target:
            left = middle + 1
        else:
            right = middle  # bug 2
    return -1  # cannot find it


if __name__ == '__main__':
    # array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    array = [100]
    print(search(array, 100))
