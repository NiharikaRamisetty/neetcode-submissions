class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for a in strs:
            abc = ''.join(sorted(a))
            ans[abc].append(a)
        return list(ans.values())