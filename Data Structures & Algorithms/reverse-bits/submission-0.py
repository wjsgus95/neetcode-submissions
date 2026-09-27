class Solution:
    def reverseBits(self, n: int) -> int:
        bits = []

        for _ in range(32):
            bits.append(n % 2)
            n >>= 1
        
        ans = 0
        power = 0
        for i in range(31, -1, -1):
            ans += bits[i] * 2 ** power
            power += 1
        return ans
        
        