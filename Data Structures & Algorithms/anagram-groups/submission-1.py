class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for i, word in enumerate(strs):
            anagrams.setdefault("".join(sorted(list(word))), []).append(word)  
        return list(anagrams.values())


        