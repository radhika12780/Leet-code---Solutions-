class Solution:
    def maxPalindromes(self, s, k):
        n = len(s)
        ans = 0
        i = 0
        
        while i <= n - k:
            # Check for palindrome of length k starting at i
            sub1 = s[i:i+k]
            if sub1 == sub1[::-1]:
                ans += 1
                i += k
                continue
            
            # Check for palindrome of length k+1 starting at i
            if i + k < n:
                sub2 = s[i:i+k+1]
                if sub2 == sub2[::-1]:
                    ans += 1
                    i += k + 1
                    continue
            
            # Move to the next index if no palindrome of length k or k+1 is found
            i += 1
            
        return ans