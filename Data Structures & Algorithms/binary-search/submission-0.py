class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            value = nums[mid]

            if value > target:
                right = mid - 1
            elif value < target:
                left = mid + 1
            else:
                return mid
        
        return -1
        