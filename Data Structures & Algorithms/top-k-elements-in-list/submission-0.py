class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        
        for n in nums:
            if n in dic:
                dic[n] +=1
            else:
                dic[n] = 1
        dic2 = dict(sorted(dic.items(), key=lambda item: item[1], reverse=True))
        lis=[k for k,v in dic2.items()]
        lis2=[lis[n] for n in range(0,k)]
        return lis2