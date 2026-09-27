class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()

        N = len(nums)
        nums.sort()

        for mid in range(1, N - 1):
            left, right = mid - 1, mid + 1

            while 0 <= left and right < N:
                if nums[left] + nums[mid] + nums[right] > 0:
                    left -= 1
                elif nums[left] + nums[mid] + nums[right] < 0:
                    right += 1
                else:
                    ans.add((nums[left], nums[mid], nums[right]))
                    left -= 1
        
        return [list(triplet) for triplet in ans]