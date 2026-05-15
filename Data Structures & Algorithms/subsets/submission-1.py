class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = [[]]

        
        for num in nums:
            # for every subset alr in res, 
            # create new subset that includes num
            # append newly made subsets to res
            res += [subset + [num] for subset in res]

        return res