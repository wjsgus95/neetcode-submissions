class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        value = 0
        digits.reverse()
        while digits:
            last = digits.pop()
            value *= 10
            value += last
        value += 1

        ans = []
        while value > 0:
            ans.append(value % 10)
            value //= 10
        
        ans.reverse()
        return ans
        