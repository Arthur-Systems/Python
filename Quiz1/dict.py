def make_dict(words):
    dictionary = {}
    for word in words:

        if len(word) in dictionary:
            dictionary[len(word)].append(word)
        elif len(word) >= 10:
            dictionary.setdefault(10, []).append(word)
        else:
            dictionary[len(word)] = [word]
    return dictionary


if __name__ == '__main__':

    d = {2: ['at', 'to', 'no'], 3: ['add', 'sun'], 10: ['Hello! How are you?']}
    dictionary = make_dict(
        ['at', 'add', 'sun', 'to', 'no', 'Hello! How are you?'])
    print(dictionary)
    assert dictionary == d
    print('Everything works correctly!')
