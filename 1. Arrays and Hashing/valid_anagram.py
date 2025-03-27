class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hm = {}
        for letter in s:
            if letter not in hm:
                hm[letter] = 0
            hm[letter] += 1
        
        for letter in t:
            if letter not in hm:
                return False
            else:
                hm[letter] -= 1
                if hm[letter] == 0:
                    del hm[letter]
        return True