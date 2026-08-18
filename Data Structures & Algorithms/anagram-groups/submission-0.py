class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs:
            t = tuple(sorted(word))
            if t not in groups:
                groups[t] = []
            groups[t].append(word)
        return [group for group in groups.values()]