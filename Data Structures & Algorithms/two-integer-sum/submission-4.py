class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        j = 0
        ans = []
        n = nums
        for i in range(len(nums)):
            for j in range(len(nums)):
                if j == i:
                    j = i+1
                if n[i] + n[j] == target:
                    ans.append(i)
                    ans.append(j)
                    return ans
                