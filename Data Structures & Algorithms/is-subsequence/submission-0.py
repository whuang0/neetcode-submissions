class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        
        """
        check if s[index] == t[index]
        if it is, we shift both s and t
        if not we shift t, until t is empty, if t is empty we return false
        """
        sp = 0
        tp = 0

        while tp < len(t) and sp < len(s): # double check this, should be while t? maybne
            
            if s[sp] == t[tp]:
                sp += 1
            tp += 1
        return sp == len(s)