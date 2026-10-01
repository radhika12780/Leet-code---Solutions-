class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # If the string length is odd, it's mathematically impossible to be balanced
        if len(s) & 1:
            return False
            
        # Global lookup encoding token keys and expected matching closing types
        # Positive values represent bit-tokens for open brackets.
        # Negative values identify closing brackets mapped to their open counterpart's token value.
        TRANSFORM = {
            '(': 1, '[': 2, '{': 3,
            ')': -1, ']': -2, '}': -3
        }
        
        # Our virtual register stack, initialized to 0
        bit_stack = 0
        
        for char in s:
            token = TRANSFORM[char]
            
            if token > 0:
                # Push: Shift left by 2 bits to make room, then bitwise OR the token
                bit_stack = (bit_stack << 2) | token
            else:
                # Pop: Peek at the last 2 bits using a bitwise mask (3 is 11 in binary)
                # If it doesn't match the positive value of our closing token, fail immediately.
                if (bit_stack & 3) != -token:
                    return False
                # Shift right by 2 bits to discard the matched open bracket
                bit_stack >>= 2
                
        # If bit_stack is exactly 0, all brackets were perfectly matched and cleared
        return bit_stack == 0
        