# Problem:
# Count Vowels in a String

# Write a function that takes a string s and returns the number of vowels (a, e, i, o, u) in it. The function should be case-insensitive.

# Example:
# python
# Copy code
# Input: s = "Hello, World!"
# Output: 3
# Explanation: The vowels are 'e', 'o', and 'o'.

# Input: s = "Python Programming"
# Output: 3
# Explanation: The vowels are 'o', 'o', and 'a'.

class VowelCounter:
    def __init__(self, text):
        """Initialize the VowelCounter with the input text."""
        self.text = text

    def count_vowels(self):
        """Count the number of vowels in the text."""
        vowels = "aeiouAEIOU"
        count = 0
        for char in self.text:
            if char in vowels:
                count += 1
        return count

# Example usage
if __name__ == "__main__":
    text1 = "Hello, World!"
    counter1 = VowelCounter(text1)
    print(f"Number of vowels in '{text1}': {counter1.count_vowels()}")  # Output: 3

    text2 = "Python Programming"
    counter2 = VowelCounter(text2)
    print(f"Number of vowels in '{text2}': {counter2.count_vowels()}")  # Output: 3