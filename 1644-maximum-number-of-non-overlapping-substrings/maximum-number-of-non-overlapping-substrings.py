class Solution:
    def maxNumOfSubstrings(self, s):
        # 1. Track first and last occurrence of each character
        first = {}
        last = {}
        for i, ch in enumerate(s):
            if ch not in first:
                first[ch] = i
            last[ch] = i

        # 2. Find valid bounds for substrings starting at first[ch]
        valid_intervals = []
        for ch in first:
            start = first[ch]
            end = last[ch]
            
            # Expand boundary if internal characters stretch further
            possible = True
            i = start
            while i <= end:
                if first[s[i]] < start:
                    possible = False
                    break
                end = max(end, last[s[i]])
                i += 1
            
            if possible:
                valid_intervals.append((start, end))

        # 3. Sort intervals by ending position (Greedy strategy)
        valid_intervals.sort(key=lambda x: x[1])

        # 4. Pick non-overlapping intervals
        res = []
        prev_end = -1
        for start, end in valid_intervals:
            if start > prev_end:
                res.append(s[start:end + 1])
                prev_end = end

        return res