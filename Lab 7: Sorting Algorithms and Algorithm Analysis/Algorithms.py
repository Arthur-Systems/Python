

def bubbleSort(items):
    swaps = 0
    for i in range(len(items)-1, 0, -1):  # generate a range for the next step
        for j in range(i):             # note that the range i is decrementing
            if items[j] > items[j+1]:
                items[j], items[j+1] = items[j+1], items[j]  # swap items
                swaps += 1
    return swaps


list_ = [54, 26, 93, 17, 77, 31, 44, 55, 20]

swaps = bubbleSort(list_)
print(list_, "swaps", swaps)


def selectionSort(items):
    count = 0
    firstswap = []

    for i in range(len(items)-1, 0, -1):
        m = 0
        for j in range(1, i+1):          # find the maximum in the range
            if items[j] > items[m]:
                m = j
        count += 1
        items[m], items[i] = items[i], items[m]
    return firstswap, count


list_ = [54, 26, 93, 17, 77, 31, 44, 55, 20]
first, count = selectionSort(list_)
print(list_, "first swap", first, "swaps", count)


def insertionSort(items):
    for i in range(1, len(items)):
        m = items[i]
        while i > 0 and items[i-1] > m:
            items[i] = items[i-1]
            i -= 1
        items[i] = m


list_ = [54, 26, 93, 17, 77, 31, 44, 55, 20]
insertionSort(list_)
print(list_)
