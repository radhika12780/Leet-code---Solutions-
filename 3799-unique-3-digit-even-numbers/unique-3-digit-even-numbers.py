class Solution:
    def totalNumbers(self, digits):
        # Count available digits
        available = {}
        for d in digits:
            available[d] = available.get(d, 0) + 1
            
        count = 0
        
        # Check every 3-digit even number
        for num in range(100, 1000, 2):
            d1 = num // 100        # Hundreds digit
            d2 = (num // 10) % 10  # Tens digit
            d3 = num % 10          # Units digit
            
            # Count required digits for current number
            req = {}
            req[d1] = req.get(d1, 0) + 1
            req[d2] = req.get(d2, 0) + 1
            req[d3] = req.get(d3, 0) + 1
            
            # Verify if we have enough digits
            possible = True
            for digit, needed in req.items():
                if available.get(digit, 0) < needed:
                    possible = False
                    break
            
            if possible:
                count += 1
                
        return count