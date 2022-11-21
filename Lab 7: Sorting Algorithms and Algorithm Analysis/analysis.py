import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from timeit import Timer, timeit
from random import choice


def bubbleSort(items):
    for i in range(len(items)-1, 0, -1):  # generate a range for the next step
        for j in range(i):             # note that the range i is decrementing
            if items[j] > items[j+1]:
                items[j], items[j+1] = items[j+1], items[j]  # swap items


def quicksort(items):
    if len(items) < 2:
        return items
    else:
        pivot = choice(items)
        less = [i for i in items if i < pivot]
        greater = [i for i in items if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)


def mergesort(items):
    if len(items) < 2:
        return items
    else:
        mid = len(items) // 2
        left = items[:mid]
        right = items[mid:]
        return merge(mergesort(left), mergesort(right))


def merge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result.extend(left)
    result.extend(right)
    return result


list_ = list(range(0, 500))      # list of numbers
d1 = [choice(list_) for i in range(10)]  # random list of size 10
d2 = [choice(list_) for i in range(20)]  # random list of size 20
d3 = [choice(list_) for i in range(50)]  # random list of size 50
d4 = [choice(list_) for i in range(100)]  # random list of size 100
d5 = [choice(list_) for i in range(200)]  # random list of size 200
d6 = [choice(list_) for i in range(500)]  # random list of size 500


# you need to add more lists of different sizes: d3, d4, d5, and d6
data = [d1, d2, d3, d4, d5, d6]  # your input
times = {}       # times required to sort input

for i in data:
    t1 = Timer(f"bubbleSort({i})", "from __main__ import bubbleSort")
    print("bubblesort ", t1.timeit(number=3), "milliseconds")  # for debugging
    times.setdefault("bubbleSort", []).append(t1.timeit(number=3))
    t2 = Timer(f"quicksort({i})", "from __main__ import quicksort")
    print("quicksort ", t2.timeit(number=3), "milliseconds")  # for debugging
    times.setdefault("quicksort", []).append(t2.timeit(number=3))
    t3 = Timer(f"mergesort({i})", "from __main__ import mergesort")
    print("mergesort ", t3.timeit(number=3), "milliseconds")  # for debugging
    times.setdefault("mergesort", []).append(t3.timeit(number=3))

# do not forget to plot your data!!!
if __name__ == "__main__":
    print(times)
    size = [10, 20, 50, 100, 200, 500]
    fig = plt.figure(tight_layout=False, figsize=(10, 8), dpi=80)
    fig.suptitle('Sorting Algorithms', fontsize=16)
    legend = ['Bubble Sort', 'Quick Sort', 'Merge Sort']
    ax = fig.add_subplot(111)
    plt.xlim(10, 550)
    plt.ylim(0, 0.1)
    ax.set_xlabel('Input Size')
    ax.set_ylabel('Time (ms)')
    ax.plot(size, times['bubbleSort'], label=legend[0])
    for x, y in zip(size, times['bubbleSort']):
        ax.annotate(f'{(y * 100):.2f} ms', (x, y),
                    textcoords="offset points", xytext=(0, 10), ha='center')
    ax.plot(size, times['quicksort'], label=legend[1])
    for x, y in zip(size, times['quicksort']):
        ax.annotate(f'{(y * 100):.2f} ms', (x, y),
                    textcoords="offset points", xytext=(0, 0), ha='center')
    ax.plot(size, times['mergesort'], label=legend[2])
    for x, y in zip(size, times['mergesort']):
        ax.annotate(f'{(y * 100):.2f} ms', (x, y),
                    textcoords="offset points", xytext=(0, 10), ha='center')
    ax.legend()
    plt.show()
