class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)
        d = {}
        if n == 0:
            return [[""]]
        if n == 1:
            return [strs]
        for i in range(n):
            key = tuple(sorted(strs[i]))
            d[key] = d.get(key, []) + [strs[i]]
        return d.values()
