class Solution(object):
    def generateParenthesis(self, n):
        result = []

        def build(current, open_count, close_count):
            # Base case: if string reaches target length (2 * n)
            if len(current) == 2 * n:
                result.append(current)
                return

            # Add an open bracket if we haven't reached n yet
            if open_count < n:
                build(current + "(", open_count + 1, close_count)

            # Add a close bracket only if it balances an open bracket
            if close_count < open_count:
                build(current + ")", open_count, close_count + 1)

        # Start recursion with an empty string and 0 counts
        build("", 0, 0)
        return result