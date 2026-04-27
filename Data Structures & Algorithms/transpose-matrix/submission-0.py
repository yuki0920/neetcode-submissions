class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        new_matrix = [[0] * ROWS for _ in range(COLS)]

        # i,j が転置すると j, iになる
        for i in range(ROWS):
            for j in range(COLS):
                new_matrix[j][i] = matrix[i][j]

        return new_matrix
