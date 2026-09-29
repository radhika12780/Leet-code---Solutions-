class Solution(object):
    def numOfStrings(self, patterns, word):
        """
        :type patterns: List[str]
        :type word: str
        :rtype: int
        """
        # Step 1: Build a Suffix Trie of the target word
        # This acts as a state machine containing every possible substring of 'word'
        root = {}
        n = len(word)
        
        for i in range(n):
            node = root
            for j in range(i, n):
                char = word[j]
                if char not in node:
                    node[char] = {}
                node = node[char]
        
        # Step 2: Track matches by traversing the state machine
        count = 0
        for pattern in patterns:
            node = root
            possible = True
            for char in pattern:
                if char in node:
                    node = node[char]
                else:
                    possible = False
                    break
            if possible:
                count += 1
                
        return count