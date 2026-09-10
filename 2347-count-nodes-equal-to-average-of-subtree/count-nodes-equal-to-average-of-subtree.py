class Solution:
    def averageOfSubtree(self, root):
        self.matching_nodes = 0

        def inspect(node):
            if not node:
                return 0, 0

            # Calculate sum and count from left and right subtrees
            left_sum, left_count = inspect(node.left)
            right_sum, right_count = inspect(node.right)

            # Total sum and count for the current node's subtree
            total_sum = left_sum + right_sum + node.val
            total_count = left_count + right_count + 1

            # Integer division automatically rounds down
            if total_sum // total_count == node.val:
                self.matching_nodes += 1

            return total_sum, total_count

        inspect(root)
        return self.matching_nodes