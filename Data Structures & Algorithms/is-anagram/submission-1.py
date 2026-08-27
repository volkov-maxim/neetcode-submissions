class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        return all(s.count(s_i) == t.count(s_i) for s_i in s)