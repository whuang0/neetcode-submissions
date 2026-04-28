class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        """
        default dict
        tally the # of char's and chars

        group them if they equal
        
        """
        result = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] += 1
            result[tuple(count)].append(s)

        return list(result.values())



