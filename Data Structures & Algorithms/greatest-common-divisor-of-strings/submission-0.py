class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) < len(str2):
            str1, str2 = str2, str1
        
        # str1をstr2で割れるか試す
        n1 = len(str1)
        n2 = len(str2)
        n = len(str2)

        while n > 0:
            div1, mod1 = divmod(n1, n)
            div2, mod2 = divmod(n2, n)
            if (mod1 == 0 and mod2 == 0 and
                str1 == str2[:n] * div1 and
                str2 == str2[:n] * div2
            ):
                return str2[:n]

            n -= 1
            
        return ""