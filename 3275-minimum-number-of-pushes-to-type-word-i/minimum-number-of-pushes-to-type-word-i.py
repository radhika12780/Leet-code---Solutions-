class Solution(object):
    def minimumPushes(self, word):
        total_pushes = 0
        
        # Loop through each letter index in the word
        for i in range(len(word)):
            # Every group of 8 letters increases the required pushes by 1
            total_pushes += (i // 8) + 1
            
        return total_pushes