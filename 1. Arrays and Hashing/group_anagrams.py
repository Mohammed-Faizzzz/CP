class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {}
        res = []

        for word in strs:
            key = "".join(sorted(word))
            if key not in hm:
                hm[key] = []
            hm[key].append(word)


        for val in hm.values():
            res.append(val)
        
        return res
        