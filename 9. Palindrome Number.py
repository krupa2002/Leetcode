# Understnding
''' If x is negative, it cannot be a palindrome because the negative sign will not match when the number is reversed.
If x is a single digit, it is trivially a palindrome.
Convert the integer to its reverse form and compare it with the original integer.
If both the original integer and the reversed integer are the same, then x is palindrome
To reverse the integer, we can convert it to a string, reverse the string, and convert it back to an integer.
Alternatively, we can reverse the integer mathematically by extracting digits from the end and building the reversed number.'''

# Code
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        # Convert the number to string
        original_str = str(x)
        # Reverse the string
        reversed_str = original_str[::-1]
        # Check if the original string is the same as the reversed string
        return original_str == reversed_str
