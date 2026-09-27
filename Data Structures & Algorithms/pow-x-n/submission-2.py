class Solution:
    def myPow(self, x: float, n: int) -> float:
        def recurse(base: int, power: int) -> float:
            if power == 0:
                return 1
            
            if power == 1:
                return base

            if power < 0:
                return 1 / recurse(base, -power)
            
            if power % 2 == 0:
                return recurse(base * base, power // 2)
            else:
                return recurse(base, power - 1) * recurse(base, 1)
            
        return recurse(x, n)