class Solution:
    def minSwaps(self, nums):
        n = len(nums)

        # Step 1: Create a list of tuples containing (digit_sum, value, original_index)
        items = []
        for i in range(n):
            num = nums[i]
            d_sum = sum(int(digit) for digit in str(num))
            items.append((d_sum, num, i))

        # Step 2: Sort based on digit sum, then by value
        items.sort()

        # Step 3: Count cycles to determine minimum swaps
        visited = [False] * n
        swaps = 0

        for i in range(n):
            # If already visited or already in the correct position, skip
            if visited[i] or items[i][2] == i:
                continue

            # Traverse the cycle
            cycle_size = 0
            curr = i
            while not visited[curr]:
                visited[curr] = True
                curr = items[curr][2]
                cycle_size += 1

            # A cycle of size K takes (K - 1) swaps
            if cycle_size > 0:
                swaps += cycle_size - 1

        return swaps