class Solution:

    def encode(self, strs: List[str]) -> str:
        newstr = ''
        for s in strs:
            newstr += str(len(s)) + "#" + s
        return newstr
        5#Hello5#World

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i 
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
    
        return res 
