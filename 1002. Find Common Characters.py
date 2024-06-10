''' # Step 1: Initialize the frequency array
common_freq = array of size 26 with all elements as inf

# Step 2: Define a function to get character count
function get_char_count(word):
    count = array of size 26 with all elements as 0
    for char in word:
        index = ord(char) - ord('a')
        count[index] += 1
    return count

# Step 3: Update the frequency array for each word
for word in words:
    word_count = get_char_count(word)
    for i from 0 to 25:
        common_freq[i] = min(common_freq[i], word_count[i])

# Step 4: Construct the result array
result = []
for i from 0 to 25:
    if common_freq[i] != inf:
        char = chr(i + ord('a'))
        for j from 0 to common_freq[i] - 1:
            result.append(char)

# Step 5: Return the result
return result'''

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common_freq = [float('inf')] * 26

        # Function to get frequency of characters in a word
        def get_char_count(word):
            count = [0] * 26
            for char in word:
                count[ord(char) - ord('a')] += 1
            return count

        # Update common_freq with the character count of each word
        for word in words:
            word_count = get_char_count(word)
            for i in range(26):
                common_freq[i] = min(common_freq[i], word_count[i])

        # Construct the result array based on common_freq
        result = []
        for i in range(26):
            if common_freq[i] != float('inf'):
                result.extend([chr(i + ord('a'))] * common_freq[i])

        return result
        
        
