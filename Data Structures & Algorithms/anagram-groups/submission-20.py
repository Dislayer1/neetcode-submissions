class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}

        for n in range(len(strs)):
            sor = tuple(sorted(strs[n]))
            if sor in dic:
                dic[sor].append(strs[n])
            else:
                dic[sor] = [strs[n]]
        
        return list(dic.values())