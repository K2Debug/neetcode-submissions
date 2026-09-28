class Solution:
    def encode(self, strs: List[str]) -> str:
        shift = 7
        result=[]
        for word in strs:
            for char in word:
                if char.isupper():
                    result += chr((ord(char) + shift - 65) % 26 + 65)
                elif char.islower():
                    result += chr((ord(char) + shift - 97) % 26 + 97)
                else:
                    result += char
            result += "#!"
        return "".join(result)

    def decode(self, s: str) -> List[str]:
        shift = 7
        result= ""
        for char in s:
            if char.isupper():
                result += chr((ord(char) - shift - 65) % 26 + 65)
            elif char.islower():
                result += chr((ord(char) - shift - 97) % 26 + 97)
            else:
                result += char
            
        return result.split("#!")[:-1]
