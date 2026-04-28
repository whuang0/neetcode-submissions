class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            middle = low + (high - low) // 2

            if nums[middle] < target:
                # half in lower
                low = middle + 1
            elif nums[middle] > target:
                # half in the upper
                high = middle - 1

            else:
                return middle
        return -1
