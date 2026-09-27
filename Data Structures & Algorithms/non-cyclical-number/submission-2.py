class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        def recurse(k: int) -> bool:
            if k == 1:
                return True
            
            if k in seen:
                return False
            seen.add(k)
            
            next_value = 0
            while k > 0:
                digit = k % 10
                next_value += digit ** 2
                k //= 10
            
            return recurse(next_value)
        
        return recurse(n)
            