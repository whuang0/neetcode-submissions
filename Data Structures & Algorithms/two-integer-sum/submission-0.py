class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} # val : index

        for i, n in enumerate(nums): # iterate through every value, need index and actual number
            diff = target - n 
            if diff in prevMap: #check if difference alr in hashmap
                return [prevMap[diff], i] #if it is return the indencies
            prevMap[n] = i # update hashmap if solution not found
        return []