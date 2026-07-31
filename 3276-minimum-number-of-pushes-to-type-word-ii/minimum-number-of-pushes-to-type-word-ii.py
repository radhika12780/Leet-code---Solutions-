class Solution:
    def minimumPushes(self, word):
        # Count the frequency of each letter in the word
        counts = {}
        for char in word:
            counts[char] = counts.get(char, 0) + 1
        
        # Sort frequencies in descending order
        frequencies = sorted(counts.values(), reverse=True)
        
        total_pushes = 0
        
        # Calculate minimum pushes using greedy approach
        for i in range(len(frequencies)):
            presses_needed = (i // 8) + 1
            total_pushes += frequencies[i] * presses_needed
            
        return total_pushes