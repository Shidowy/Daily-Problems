# Input: s1 = "Listen", s2 = "Silent"
# Output: True
# Explanation: Both strings can be rearranged to form "Listen".

# Input: s1 = "Hello", s2 = "World"
# Output: False

import string

class AnagramChecker:
    def __init__(self, str1, str2):
        """Initialize the AnagramChecker with two input strings."""
        self.str1 = str1
        self.str2 = str2

    def normalize_string(self, s):
        """Normalize the string by converting to lowercase, removing spaces, and punctuation."""
        s = s.lower()  # Convert to lowercase
        s = s.replace(" ", "")  # Remove spaces
        s = s.translate(str.maketrans("", "", string.punctuation))  # Remove punctuation
        return s
    
    def are_anagrams(self):
        """Check if the two strings are anagrams of each other."""
        normalized_str1 = self.normalize_string(self.str1)
        normalized_str2 = self.normalize_string(self.str2)
        return sorted(normalized_str1) == sorted(normalized_str2)


# Example usage
if __name__ == "__main__":
    checker1 = AnagramChecker("Listen", "Silent")
    print(f"Are they anagrams? {checker1.are_anagrams()}")  # Output: True

    checker2 = AnagramChecker("Hello", "World")
    print(f"Are they anagrams? {checker2.are_anagrams()}")  # Output: False