class Solution:
    def findMin(self, nums: List[int]) -> int:
        N = len(nums)
        left, right = 0, N - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] < nums[mid-1]:
                return nums[mid]

            if nums[mid] < nums[left]:
                right = mid - 1
            elif nums[mid] > nums[right]:
                left = mid + 1
            else:
                return nums[left]
        
        return nums[mid]