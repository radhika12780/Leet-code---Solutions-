class Solution:
    def lexicographicallySmallestArray(self, nums, limit):
        n = len(nums)
        
        # Keep track of original values and their original indices
        sorted_pairs = sorted((nums[i], i) for i in range(n))
        
        groups = []
        current_group = [sorted_pairs[0]]
        
        # Group numbers together if the step between consecutive sorted elements is <= limit
        for i in range(1, n):
            if sorted_pairs[i][0] - sorted_pairs[i - 1][0] <= limit:
                current_group.append(sorted_pairs[i])
            else:
                groups.append(current_group)
                current_group = [sorted_pairs[i]]
        groups.append(current_group)
        
        result = [0] * n
        
        # For each connected group, place sorted values back into sorted original positions
        for group in groups:
            indices = sorted(idx for val, idx in group)
            values = [val for val, idx in group]
            
            for i in range(len(group)):
                result[indices[i]] = values[i]
                
        return result