class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        maxSeen = 0
        for i in nums:
            if i == 1:
                count += 1
                maxSeen = max(maxSeen, count)
            else:
                count = 0
        return maxSeen