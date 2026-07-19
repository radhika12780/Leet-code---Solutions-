class Solution:
    def smallestSubsequence(self, s):
        # Map each character to its last seen index
        last_pos = {char: i for i, char in enumerate(s)}
        
        stack = []
        seen = set()
        
        for i, char in enumerate(s):
            if char in seen:
                continue
                
            # If the current char is smaller than the top of the stack,
            # and that stack char appears again later, we can pop it.
            while stack and char < stack[-1] and last_pos[stack[-1]] > i:
                seen.remove(stack.pop())
                
            stack.append(char)
            seen.add(char)
            
        return "".join(stack)