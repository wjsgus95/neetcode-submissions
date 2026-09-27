class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        negative = n < 0
        if negative:
            n = -n

        memo = [None] * (n + 1)
        memo[0] = 1
        memo[1] = x
        power = 2
        while power <= n:
            memo[power] = memo[power//2] * memo[power//2]
            power *= 2

        def recurse(power: int) -> float:
            if memo[power] is not None:
                return memo[power]
            
            factor = 1
            while factor * 2 < power:
                factor *= 2
            return memo[factor] * recurse(power - factor)
        
        value = recurse(n)
        if negative:
            return 1 / value
        return value