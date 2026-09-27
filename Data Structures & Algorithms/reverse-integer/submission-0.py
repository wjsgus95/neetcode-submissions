class Solution:
    def reverse(self, x: int) -> int:
        negative = x < 0
        x = -x if negative else x

        ans = 0
        while x > 0:
            r = x % 10

            ans *= 10
            ans += r

            x //= 10
        
        if ans > 2**31 - 1:
            return 0

        ans = -ans if negative else ans
        return ans