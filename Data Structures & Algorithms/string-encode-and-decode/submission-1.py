class Solution:
    def encode(self, strs: List[str]) -> str:
        result = []

        for word in strs:
            result.append(word)
            result.append("#!")

        return "".join(result)

    def decode(self, s: str) -> List[str]:
        return s.split("#!")[:-1]
