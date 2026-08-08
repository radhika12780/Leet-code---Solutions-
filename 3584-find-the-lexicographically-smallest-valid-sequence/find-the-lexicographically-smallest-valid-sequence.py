class Solution:
    def validSequence(self, word1, word2):
        n = len(word1)
        m = len(word2)

        # last_pos[j] stores the largest index in word1 
        # from where word2[j:] can be matched as a subsequence
        last_pos = [-1] * m
        
        ptr = n - 1
        for j in range(m - 1, -1, -1):
            while ptr >= 0 and word1[ptr] != word2[j]:
                ptr -= 1
            if ptr >= 0:
                last_pos[j] = ptr
                ptr -= 1

        ans = []
        changed = False
        ptr1 = 0

        for ptr2 in range(m):
            found = False
            
            while ptr1 < n:
                # Option 1: Exact character match
                if word1[ptr1] == word2[ptr2]:
                    ans.append(ptr1)
                    ptr1 += 1
                    found = True
                    break
                
                # Option 2: Mismatch, but we can change this character
                # Check if the remaining suffix word2[ptr2 + 1:] can still be matched
                if not changed:
                    can_finish = (ptr2 + 1 == m) or (last_pos[ptr2 + 1] > ptr1)
                    if can_finish:
                        ans.append(ptr1)
                        changed = True
                        ptr1 += 1
                        found = True
                        break
                
                ptr1 += 1

            if not found:
                return []

        return ans