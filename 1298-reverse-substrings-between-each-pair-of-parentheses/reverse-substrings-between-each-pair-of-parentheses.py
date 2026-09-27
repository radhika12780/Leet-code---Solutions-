class Solution:
    def reverseParentheses(self, s):
        n = len(s)
        pair = {}
        stack = []

        # Find matching pairs of parentheses
        for i in range(n):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                left = stack.pop()
                pair[left] = i
                pair[i] = left

        # Traversal using teleportation trick
        res = []
        curr = 0
        step = 1

        while curr < n:
            if s[curr] in '()':
                curr = pair[curr]
                step = -step
            else:
                res.append(s[curr])
            curr += step

        return "".join(res)