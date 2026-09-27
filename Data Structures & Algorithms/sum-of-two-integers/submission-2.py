class Solution:
    def getSum(self, a: int, b: int) -> int:
        carry = 0
        ans = 0
        mask = 0xffffffff

        for i in range(32):
            a_bit = a & 1
            b_bit = b & 1

            current = a_bit ^ b_bit ^ carry
            carry = (a_bit & b_bit) | (carry & (a_bit | b_bit))

            if current:
                ans |= (1 << i)

            a >>= 1
            b >>= 1
        
        if ans > 0x7fffffff:
            ans = ~(ans ^ mask)
        
        return ans