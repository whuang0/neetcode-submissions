class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Frequency counter of the characters
        # so initialize a 26 [0] ch array for all the alphabet letters
        res = defaultdict(list)

        for word in strs:
            count = 26 * [0]

            for char in word:
                count[ord(char) - ord('a')] += 1
            res[tuple(count)].append(word)
        return list(res.values())

        # key value pairing for letters : #'s it appears


