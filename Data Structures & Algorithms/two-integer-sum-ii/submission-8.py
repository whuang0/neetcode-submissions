class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # array = [1, 2, 3 ...]
        # return index of two numbers [index of 1, index of 2] 
        # value of indice 1 has to be les than indice 2, use unique elements
        # cant use same index.

        """ 
        brute force approach, check every number in numbers, 
        and see if they add to the target
        """

        # get the value/index of each number in n
        index = []
        remaingVal = 0
        
        # touch up on enumerate, index/value pair, implementation touchup
        for i in range(len(numbers)):
            # 3 - 1 = 2
            for j in range(i+1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return [i + 1, j + 1]



        