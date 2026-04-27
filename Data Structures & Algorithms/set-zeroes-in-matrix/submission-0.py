class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        H = len(matrix)
        W = len(matrix[0])
        # 0が見つかった時にほかを更新するが、更新されたことによる0なのかどうかを判別する
        updated = [[False] * W for _ in range(H)]

        for i in range(H):
            for j in range(W):
                if matrix[i][j] == 0 and not updated[i][j]:
                    for k in range(W):
                        if matrix[i][k] == 0:
                            continue
                        matrix[i][k] = 0
                        updated[i][k] = True

                    for l in range(H):
                        if matrix[l][j] == 0:
                            continue
                        matrix[l][j] = 0
                        updated[l][j] = True