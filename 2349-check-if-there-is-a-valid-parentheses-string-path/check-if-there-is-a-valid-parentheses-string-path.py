class Solution(object):
    def hasValidPath(self, grid):
        rows = len(grid)
        cols = len(grid[0])

        # If total path length is odd, it's impossible to form balanced parentheses
        if (rows + cols - 1) % 2 != 0:
            return False

        # If starting cell is ')' or ending cell is '(', it can never be valid
        if grid[0][0] == ')' or grid[rows - 1][cols - 1] == '(':
            return False

        memo = {}

        def find_path(r, c, open_brackets):
            # Update open parentheses count for current cell
            if grid[r][c] == '(':
                open_brackets += 1
            else:
                open_brackets -= 1

            # If closed brackets exceed open ones at any point, invalid path
            if open_brackets < 0:
                return False

            # Reached destination: check if all brackets are properly matched
            if r == rows - 1 and c == cols - 1:
                return open_brackets == 0

            # Memoization key to avoid redundant work
            state = (r, c, open_brackets)
            if state in memo:
                return memo[state]

            # Try moving down
            down_path = False
            if r + 1 < rows:
                down_path = find_path(r + 1, c, open_brackets)

            # Try moving right (if down path didn't already succeed)
            right_path = False
            if not down_path and c + 1 < cols:
                right_path = find_path(r, c + 1, open_brackets)

            memo[state] = down_path or right_path
            return memo[state]

        return find_path(0, 0, 0)