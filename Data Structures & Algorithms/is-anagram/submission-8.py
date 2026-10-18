class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        ss = sorted(list(s))
        tt = sorted(list(t))
        if ss == tt:
            return True
        else:
            return False