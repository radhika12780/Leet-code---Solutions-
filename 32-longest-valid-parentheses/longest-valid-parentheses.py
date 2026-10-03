class Solution:
    def longestValidParentheses(self, s):
        ans = 0

        # Scan Left to Right
        left = 0
        right = 0
        for ch in s:
            if ch == "(":
                left += 1
            else:
                right += 1

            if left == right:
                ans = max(ans, 2 * right)
            elif right > left:
                left = 0
                right = 0

        # Scan Right to Left
        left = 0
        right = 0
        for ch in reversed(s):
            if ch == "(":
                left += 1
            else:
                right += 1

            if left == right:
                ans = max(ans, 2 * left)
            elif left > right:
                left = 0
                right = 0

        return ans