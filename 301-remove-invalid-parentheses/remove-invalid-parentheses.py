class Solution:
    def removeInvalidParentheses(self, s):
        def is_valid(text):
            count = 0
            for char in text:
                if char == '(':
                    count += 1
                elif char == ')':
                    count -= 1
                    if count < 0:
                        return False
            return count == 0

        queue = [s]
        visited = {s}
        result = []
        found = False

        while queue:
            current = queue.pop(0)

            if is_valid(current):
                result.append(current)
                found = True

            if found:
                continue

            for i in range(len(current)):
                if current[i] not in "()":
                    continue

                nxt = current[:i] + current[i+1:]
                if nxt not in visited:
                    visited.add(nxt)
                    queue.append(nxt)

        return result