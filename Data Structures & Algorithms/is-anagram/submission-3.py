class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ss = set(s)
        if ss != set(t): 
            return False
        dict1 = {}
        dict2 = {}
        for i in ss:
            dict1[i] = s.count(i)
            dict2[i] = t.count(i)

        if dict1 == dict2:
            return True
        return False