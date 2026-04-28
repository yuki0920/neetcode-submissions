class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
            
        len1 = len(num1)
        len2 = len(num2)

        res = [0] * (len1 + len2)
        for i in range(len1-1, -1, -1):
            for j in range(len2-1, -1, -1):
                mul = int(num1[i]) * int(num2[j])
                p1 = i + j
                p2 = i + j + 1

                # 現状の合計を出し、10で割った商を上位に、余りを下位に割り当てる
                total = mul + res[p2]
                res[p2] = total % 10
                res[p1] += total // 10

                print(num1[i], num2[j], res)

        # 最後は左側の0を削って終わり
        return ''.join(map(str, res)).lstrip('0')