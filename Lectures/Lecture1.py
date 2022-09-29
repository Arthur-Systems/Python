from timeit import Timer, timeit
import csv

# this function work only with strings composed of unique letters!


def is_anagram1(s1, s2):
    if len(s1) != len(s2):
        return False
    else:
        for i in range(len(s1)):
            found = False
            for j in range(len(s1)):
                if s1[i] == s2[j]:
                    found = True
                    break
            if not found:
                return False
        return True

# this function works with any strings


def is_anagram2(s1, s2):
    if len(s1) != len(s2):
        return False
    s1 = sorted(list(s1))
    s2 = sorted(list(s2))
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return False
    return True

# this function works with any strings


def is_anagram3(s1, s2):
    c1 = [0]*26
    c2 = [0]*26

    for i in range(len(s1)):
        pos = ord(s1[i])-ord('a')
        c1[pos] = c1[pos] + 1

    for i in range(len(s2)):
        pos = ord(s2[i])-ord('a')
        c2[pos] = c2[pos] + 1

    for j in range(len(c1)):
        if c1[j] != c2[j]:
            return False
    return True


def analyze(func):
    word = ['ab', 'abc', 'abcd', 'abcde', 'abcdef',
            'abcdefg', 'abcdefgh', 'abcdefghi', 'abcdefghij', 'abcdefghijk', 'abcdefghijkl', 'abcdefghijklm', 'abcdefghijklmn', 'abcdefghijklmno', 'abcdefghijklmnop', 'abcdefghijklmnopq', 'abcdefghijklmnopqr', 'abcdefghijklmnopqrs', 'abcdefghijklmnopqrst', 'abcdefghijklmnopqrstu', 'abcdefghijklmnopqrstuv', 'abcdefghijklmnopqrstuvw', 'abcdefghijklmnopqrstuvwx', 'abcdefghijklmnopqrstuvwxy', 'abcdefghijklmnopqrstuvwxyz']

    reverse = [x[::-1] for x in word]

    # printing Aligned Header
    print('{:<30} {:<30} {:<20} {:<20}'.format(
        'Word:', 'Reversed:', 'Result:', 'Time:'))
    for i in range(len(word)):

        print(
            f'{word[i]:<30} {reverse[i]:<30} {func(word[i], reverse[i])!s:<20} {timeit(lambda: func(word[i], reverse[i]), number=10000):<20.10f}')
    print("\n")


if __name__ == '__main__':
    analyze(is_anagram1)

    analyze(is_anagram2)

    analyze(is_anagram3)
