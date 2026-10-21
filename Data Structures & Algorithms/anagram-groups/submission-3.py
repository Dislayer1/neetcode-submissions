class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lis = []
        dic = defaultdict(list)
        added = False
        for n in range(len(strs)):
            added = False
            if tuple(sorted(strs[n])) in dic:
                dic[tuple(sorted(strs[n]))].append(strs[n])
                added = True
            else:
                dic[tuple(sorted(strs[n]))] = [strs[n]]
        
        return list(dic.values())