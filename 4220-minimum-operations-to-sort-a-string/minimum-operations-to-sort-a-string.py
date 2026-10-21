class Solution:
    def minOperations(self, s):
        # 1. Already sorted check
        if s == "".join(sorted(s)):
            return 0
            
        # 2. Length 2 unsorted string cannot be split
        if len(s) == 2:
            return -1
            
        smallest = min(s)
        largest = max(s)
        
        # 3. Best case: smallest at index 0 OR largest at index -1
        if s[0] == smallest or s[-1] == largest:
            return 1
            
        # 4. Worst case ("edc" pattern): single largest at start AND single smallest at end
        if s[0] == largest and s[-1] == smallest and s.count(largest) == 1 and s.count(smallest) == 1:
            return 3
            
        # 5. All other normal cases
        return 2