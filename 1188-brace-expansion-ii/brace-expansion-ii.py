class Solution(object):
    def braceExpansionII(self, expression):
        queue = [expression]
        seen = set()
        result = set()

        while queue:
            curr = queue.pop(0)

            # If there are no braces left, it's a valid completed word
            if '}' not in curr:
                result.add(curr)
                continue

            # Find the first closing brace and its matching opening brace
            right = curr.find('}')
            left = curr.rfind('{', 0, right)

            # Split the inner expression by commas
            prefix = curr[:left]
            suffix = curr[right + 1:]
            options = curr[left + 1:right].split(',')

            # Reconstruct expressions and process next ones
            for item in options:
                new_expr = prefix + item + suffix
                if new_expr not in seen:
                    seen.add(new_expr)
                    queue.append(new_expr)

        return sorted(list(result))