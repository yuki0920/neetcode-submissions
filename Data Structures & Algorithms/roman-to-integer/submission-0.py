class Solution:
    def romanToInt(self, s: str) -> int:
        dicts = {
            'I': 1, 
            'V': 5, 
            'X': 10, 
            'L': 50, 
            'C': 100, 
            'D': 500, 
            'M': 1000
        }

        symbols = list(s)
        N = len(symbols)
        prev = dicts[symbols[0]]
        ans = 0

        for i in range(1, N):
            current_symbol = symbols[i]
            current = dicts[current_symbol]
            if prev < current:
                ans -= prev
            else:
                ans += prev

            prev = current

        ans += prev

        return ans
            
