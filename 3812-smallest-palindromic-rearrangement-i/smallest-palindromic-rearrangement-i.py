class Solution:
    def smallestPalindrome(self, s):
        half = len(s) // 2
        
        # Sort the first half of characters
        left = "".join(sorted(s[:half]))
        
        # Middle character if string length is odd
        mid = s[half] if len(s) % 2 != 0 else ""
        
        # Combine left half, middle, and reversed left half
        return left + mid + left[::-1]