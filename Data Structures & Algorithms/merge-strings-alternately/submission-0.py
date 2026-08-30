class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n1, n2 = len(word1), len(word2)
        result = []
        i = 0

        while i < min(n1, n2):
            result.append(word1[i])
            result.append(word2[i])
            i += 1
        result.append(word1[i:])
        result.append(word2[i:])

        return "".join(result)