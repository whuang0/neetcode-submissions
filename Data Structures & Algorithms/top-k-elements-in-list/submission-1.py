from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # keep track of the numbers in nums and how many times they show up
        frequencyCounter = Counter(nums)
        # kind of want use a hashmap key value pairs but wouldnt we have to sort by
        # frequency? would this still be optimal?

        sortItems = sorted(frequencyCounter.items(), key = lambda x:x[1], reverse = True)

        topK = [num for num, count in sortItems[:k]]
        return topK