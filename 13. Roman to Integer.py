# Understanding 
''' Function Definition:
The function romanToInt is defined to take a single argument s of type str.
Dictionary Initialization:
The roman_to_int dictionary maps Roman numeral characters to their integer values.
Initialization of total and length:
total is initialized to 0 to store the result.
length holds the length of the input string s.
Loop Through the String:
The loop iterates over each character in the string s.
If the current character is not the last one and its value is less than the value of the next character, it indicates a subtraction scenario, so subtract the current character's value from total.
Otherwise, add the current character's value to total.
Return the Result:
The return total statement returns the final computed integer value after the loop completes. '''
# Code

class Solution:
    def romanToInt(self, s: str) -> int:
  
        roman_to_int = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0
        length = len(s)
        
        for i in range(length):
        
            if i < length - 1 and roman_to_int[s[i]] < roman_to_int[s[i + 1]]:
                total -= roman_to_int[s[i]]
            else:
                total += roman_to_int[s[i]]
        
        return total
