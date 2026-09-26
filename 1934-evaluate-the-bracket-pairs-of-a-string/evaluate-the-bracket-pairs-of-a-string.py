class Solution:
    def evaluate(self, s, knowledge):
        # Convert knowledge array to a hash map for fast O(1) lookups
        lookup = dict(knowledge)
        
        result = []
        key = []
        inside_bracket = False
        
        for char in s:
            if char == '(':
                inside_bracket = True
                key = []
            elif char == ')':
                inside_bracket = False
                key_str = "".join(key)
                # Fetch value from lookup table or default to '?'
                result.append(lookup.get(key_str, '?'))
            elif inside_bracket:
                key.append(char)
            else:
                result.append(char)
                
        return "".join(result)