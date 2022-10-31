def permute(items_original):
    if len(items_original) == 1:
        yield items_original
    else:
        for items_permuted in permute(items_original[1:]):
            for i in range(len(items_original)):
                yield items_permuted[:i] + items_original[0:1] + items_permuted[i:]


def import_dictionary(filename):
    dictionary = []
    try:
        f = open(filename, "rt")
        for word in f:
            dictionary.append(word.strip())
        f.close()
    except FileNotFoundError:
        print("The file", filename,
              "does not exist. The program will be terminated.")
        exit()
    return dictionary


def anagram(word):
    dictionary = import_dictionary(filename)
    for i in permute(word):
        if i in dictionary:
            yield i


if __name__ == '__main__':

    word = "mane"
    filename = "dictionary.txt"
    print(list(anagram(word)))
