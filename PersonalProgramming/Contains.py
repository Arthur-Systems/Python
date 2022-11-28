# class queue:
#     def __init__(self):
#         self.items = []

#     def isEmpty(self):
#         return self.items == []

#     def enqueue(self, item):
#         self.items.insert(0, item)

#     def dequeue(self):
#         return self.items.pop()

#     def size(self):
#         return len(self.items)

#     def __str__(self):
#         return str(self.items)

# m characters in word
# n characters in search
# what is the complixity of this algorithm
def contains(word, search: str) -> bool:
    for letter in search:
        for char in word:
            if letter != char:
                word = word[1:] if search[0] != char else word
                return contains(word, search)
            else:
                word = word[1:]
                break
        else:
            return False
    return True


# word = "acbbbb"
# search = "abc"

# word = "axbcde"
# search = "abcde"

# word = "abcdefabcdefabcdefabcgdef"
# search = "abcdefg"

# word: ....(i)....(i+j)..........|.......
# search:      ...(j)........|

def helper(word, index, search) -> bool:
    for j in range(len(search)):
        if index + j >= len(word):
            return False
        if word[index + j] != search[j]:
            return False
    return True


def contains(word, search: str) -> bool:
    for index in range(len(word)):
        if helper(word, index, search):
            return True
    return False


if __name__ == "__main__":
    # word = "Hello"
    # search = "Hell"
    # print(contains(word, search))

    # assert contains("abcdefabcdefabcdefabcgdefabcdef", "abcdefg") == False
    # assert contains("abcdefabcdefgabcdefabcgdefabcdefg", "abcdefg") == True
    # assert contains("abcdefabcdefgabcdefabcgdefabcdef", "abcdefg") == True
    # assert contains("aabcde", "abcde") == True
    assert contains("acbbbb", "abc") == False

    print("All tests passed")
