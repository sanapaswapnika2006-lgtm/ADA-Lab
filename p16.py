
from typing import List
import random


def strStr(haystack: str, needle: str) -> int:
    if needle == "":
        return 0

    # Build the LPS (Longest Prefix Suffix) array
    lps = [0] * len(needle)
    length = 0
    i = 1

    while i < len(needle):
        if needle[i] == needle[length]:
            length += 1
            lps[i] = length
            i += 1
        elif length > 0:
            length = lps[length - 1]
        else:
            lps[i] = 0
            i += 1

    # Search for the pattern in the text
    i = j = 0

    while i < len(haystack):
        if haystack[i] == needle[j]:
            i += 1
            j += 1

            if j == len(needle):
                return i - j

        elif j > 0:
            j = lps[j - 1]
        else:
            i += 1

    return -1


class Randomizer:
    def __init__(self, stream=None):
        self.stream = stream if stream is not None else []

    def getRandom(self) -> int:
        # Reservoir sampling: select one element uniformly
        chosen = None
        count = 0

        for item in self.stream:
            count += 1
            if random.randrange(count) == 0:
                chosen = item

        if count == 0:
            raise ValueError("Stream is empty")

        return chosen


# KMP example
haystack = input("Enter text: ")
needle = input("Enter pattern: ")
print("Pattern index:", strStr(haystack, needle))

# Randomizer example
data = [10, 20, 30, 40, 50]
r = Randomizer(data)
print("Random element:", r.getRandom())
