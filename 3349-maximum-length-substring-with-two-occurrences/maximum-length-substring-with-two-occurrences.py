class Solution:
    def maximumLengthSubstring(self, s):
        counts = {}
        left = 0
        max_len = 0
        
        for right in range(len(s)):
            char = s[right]
            counts[char] = counts.get(char, 0) + 1
            
            # Shrink the window if a character appears more than twice
            while counts[char] > 2:
                left_char = s[left]
                counts[left_char] -= 1
                left += 1
            
            # Update the maximum valid window length
            current_len = right - left + 1
            if current_len > max_len:
                max_len = current_len
                
        return max_len