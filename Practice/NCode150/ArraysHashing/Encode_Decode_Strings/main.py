class Solution:
    def encode(self, strs: list[str]) -> str: 
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
            print(res)
        return res

    def decode(self, s: str) -> list[str]:
        res = []
        i = 0
        while i < len(s):
            j = i 
            while s[j] != '#':
    

strs = ["Kuma", "Code"]    
sol = Solution()
sol.encode(strs)
