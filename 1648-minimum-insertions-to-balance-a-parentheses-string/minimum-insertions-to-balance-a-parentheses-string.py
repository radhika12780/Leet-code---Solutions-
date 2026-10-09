class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        insertions = 0
        needed_right = 0
        
        i = 0
        while i < len(s):
            if s[i] == '(':
                # Each '(' needs 2 ')'
                needed_right += 2
                # If we had an odd number of needed ')', we must add one ')'
                if needed_right % 2 != 0:
                    insertions += 1
                    needed_right -= 1
            else:
                # We encountered a ')'
                needed_right -= 1
                if needed_right < 0:
                    # We found an extra ')', so we insert '(' to balance it, 
                    # which needs 2 ')' total, minus the 1 we just saw.
                    insertions += 1
                    needed_right += 2
            i += 1
            
        return insertions + needed_right