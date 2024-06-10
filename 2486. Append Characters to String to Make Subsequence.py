
# Undestanding Problem
'''
A subsequence is derived from another string by deleting some or no characters without changing the order of the remaining characters.
For 𝑡 to be a subsequence of 𝑠, all characters of 𝑡 must appear in 𝑠 in the same order, though not necessarily consecutively
If 𝑡 is already a subsequence of 𝑠,then no characters need to be appended. This can be checked with a simple iteration through both strings.
Use two pointers, one for 𝑠 and one for 𝑡. Traverse both strings to see how much of 𝑡 is already a subsequence of 𝑠
Start matching tfrom the beginning with s using the two pointers.

For each character in s that matches the current character in t , move the pointer in t forward.
At the end of the traversal, the pointer in t will tell us how many characters have been matched.
The remaining characters in t (from the current pointer position to the end of t are the ones that need to be appended to s.
The number of characters to be appended is simply the length of t minus the number of characters that were matched during the traversal of s. '''
# Algorithm
''' Initialize two pointers, i for s and j for t .
Traverse through s :
If s[i] matches t[j] , increment j .
Increment i regardless of whether a match was found.
After the loop, j will indicate the number of characters in t that have been matched.
The result is the number of characters that are unmatched, which is text{len}(t) - j . '''
# Code
class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                j += 1
            i += 1
        return len(t) - j
