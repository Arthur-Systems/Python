def linearSearch(list_, item):
    index, found = -1, False
    for i in range(len(list_)):
        if list_[i] == item:
            found = True
            index = i
            break
    return index


test = [1, 2, 32, 8, 17, 19, 42, 13, 0]
print(linearSearch(test, 3))

print(linearSearch(test, 1))

print(linearSearch(test, 17))

print(linearSearch(test, 0))


def binarySearch(alist, item):
    first, last = 0, len(alist)-1
    index, found = -1, False
    while first <= last:
        midpoint = (first + last)//2
        if alist[midpoint] == item:
            found = True
            index = midpoint
            break
        else:
            if item < alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
    return index


testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(binarySearch(testlist, 3))
print(binarySearch(testlist, 1))
print(binarySearch(testlist, 17))
print(binarySearch(testlist, 0))

test = [1, 2, 32, 8, 17, 19, 42, 13, 0]
# simple hashing based on the modulo operation
index = [x % 9 for x in test]

# folding hash function
k = 0
for item in test:
    s = 0
    item = str(item)
    for i in item:
        s += int(i)
    index[k] = s % len(test)
    k += 1
print(index)

# mid-square hash function
k = 0
for item in test:
    item = str(item*item)
    s = item
    # print(s)
    if len(item) > 1:
        #print(len(item)//2, len(item)//2 + 1)
        s = item[len(item)//2-1] + item[len(item)//2]
    index[k] = int(s) % len(test)
    k += 1
print(index)


def hash(astring, size):
    sum = 0
    for pos in range(len(astring)):
        sum = sum + ord(astring[pos])
    return sum % size


test2 = ['cat', 'dog', 'horse', 'cow', 'bird', 'turtle', 'rabbit']
print(test2)
hashes = [hash(x, len(test2)) for x in test2]
print(hashes)
