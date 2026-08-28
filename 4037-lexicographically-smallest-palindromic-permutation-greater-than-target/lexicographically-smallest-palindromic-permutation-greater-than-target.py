class Solution:
    def lexPalindromicPermutation(self, s, target):
        counts = {}
        for char in s:
            counts[char] = counts.get(char, 0) + 1
            
        n = len(s)
        half_len = n // 2
        
        odd_chars = [c for c, cnt in counts.items() if cnt % 2 == 1]
        if len(odd_chars) > 1:
            return ""
        
        mid_char = odd_chars[0] if odd_chars else ""
        half_counts = {c: cnt // 2 for c, cnt in counts.items()}
        
        def make_palindrome(half, middle):
            return half + middle + half[::-1]
        
        best = None
        
        # Try matching prefix lengths from 0 to half_len
        for match_len in range(half_len + 1):
            curr_prefix = target[:match_len]
            
            prefix_counts = {}
            for c in curr_prefix:
                prefix_counts[c] = prefix_counts.get(c, 0) + 1
                
            can_build = True
            for c, cnt in prefix_counts.items():
                if cnt > half_counts.get(c, 0):
                    can_build = False
                    break
            if not can_build:
                continue
                
            rem_counts = {}
            for c, cnt in half_counts.items():
                used = prefix_counts.get(c, 0)
                if cnt > used:
                    rem_counts[c] = cnt - used
                    
            sorted_avail = sorted(rem_counts.keys())
            
            # Case 1: Exact match on half_len prefix
            if match_len == half_len:
                rem_half = ""
                for c in sorted_avail:
                    rem_half += c * rem_counts[c]
                candidate = make_palindrome(curr_prefix + rem_half, mid_char)
                if candidate > target:
                    if best is None or candidate < best:
                        best = candidate
                continue

            # Case 2: Diverge at index match_len with a strictly greater character
            pivot_target_char = target[match_len]
            for char in sorted_avail:
                if char > pivot_target_char:
                    temp_counts = rem_counts.copy()
                    temp_counts[char] -= 1
                    if temp_counts[char] == 0:
                        del temp_counts[char]
                        
                    rem_half = ""
                    for c in sorted(temp_counts.keys()):
                        rem_half += c * temp_counts[c]
                        
                    first_half = curr_prefix + char + rem_half
                    candidate = make_palindrome(first_half, mid_char)
                    
                    if candidate > target:
                        if best is None or candidate < best:
                            best = candidate
                    break  # Smallest valid character chosen for this prefix length

        return best if best is not None else ""