class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for i, word in enumerate(strs):
            key = "".join(sorted(list(word)))
            anagrams.setdefault(key, []).append(word)  
        return list(anagrams.values())


        