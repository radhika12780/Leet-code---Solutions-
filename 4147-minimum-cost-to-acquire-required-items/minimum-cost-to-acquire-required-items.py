class Solution:
    def minimumCost(self, cost1, cost2, costBoth, need1, need2):
        # Case 1: Buy only separate items for type 1 and type 2
        cost_separate = (need1 * cost1) + (need2 * cost2)
        
        # Case 2: Use type 3 items to cover the shared overlap min(need1, need2)
        shared_needs = min(need1, need2)
        rem1 = need1 - shared_needs
        rem2 = need2 - shared_needs
        
        cost_shared = (shared_needs * min(costBoth, cost1 + cost2)) + (rem1 * min(cost1, costBoth)) + (rem2 * min(cost2, costBoth))
        
        # Case 3: Use type 3 items to cover ALL requirements max(need1, need2)
        max_needs = max(need1, need2)
        cost_all_both = max_needs * costBoth
        
        return min(cost_separate, cost_shared, cost_all_both)