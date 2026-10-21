class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lis = []
        dic = defaultdict(list)

        for n in range(len(strs)):
            if tuple(sorted(strs[n])) in dic:
                dic[tuple(sorted(strs[n]))].append(strs[n])
            else:
                dic[tuple(sorted(strs[n]))] = [strs[n]]
        
        return list(dic.values())