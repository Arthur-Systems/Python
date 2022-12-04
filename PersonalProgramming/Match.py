class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) == len(word2):
            for x in range(len(word1)):
                for y in range(len(word2)):
                    print(word1[x], word2[y])
                    if word1[x] == word2[y]:
                        print("Match1")
                        break
                    elif y >= len(word2)-1:
                        return False
            return True
        else:
            return False


if __name__ == "__main__":
    word1 = "abca"
    word2 = "cbaf"
    sol = Solution()
    print(sol.closeStrings(word1, word2))
    assert sol.closeStrings(word1, word2) == False
