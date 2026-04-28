class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set() # Create a set
        for n in nums: #iterate through the nums in the list
            if n in hashset: # found a duplicate
                return True
            else: # otherwise add n to the set
                hashset.add(n)
        return False

        