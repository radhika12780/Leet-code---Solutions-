class Solution(object):
    def scoreOfParentheses(self, s):
        total_score = 0
        depth = 0

        for i in range(len(s)):
            if s[i] == '(':
                depth += 1
            else:
                depth -= 1
                if s[i - 1] == '(':
                    total_score += 1 << depth

        return total_score