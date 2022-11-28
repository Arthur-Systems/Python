def checkpalindrome(string):
    for i in range(len(string)):
        if string[i] != string[-i-1]:
            return False
    return True


def FindLongestPalindrome(string):
    longest = ""
    for i in range(len(string)):
        for j in range(len(string)):
            if checkpalindrome(string[i:j+1]) and len(string[i:j+1]) > len(longest):
                longest = string[i:j+1]
    return longest


def FindLongestPalindrome2(string):
    longest = ""
    for length in range(len(string)):
        pass


if __name__ == "__main__":
    string = "abccba"
    print(FindLongestPalindrome(string))
