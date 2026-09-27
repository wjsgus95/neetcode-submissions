class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def find_min() -> int:
            left, right = 0, len(nums) - 1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] < nums[right]:
                    right = mid
                else:
                    left = mid + 1
            
            return mid
        
        def binary_search(left: int, right: int) -> int:
            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            
            return -1

        min_index = find_min()
        print(min_index)
        
        left_search = binary_search(0, min_index - 1)
        if left_search != -1:
            return left_search
        
        return binary_search(min_index, len(nums) - 1)