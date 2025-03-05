class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix  
    def get_adjacent(self, row, col):
        adjacent = []
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  
        for move in moves:
            new_row, new_col = row + move[0], col + move[1]
            if new_row < 0 or new_row >= len(self.matrix):
                continue  
            if new_col < 0 or new_col >= len(self.matrix[0]):
                continue  
            adjacent.append(self.matrix[new_row][new_col])
        return adjacent
matrix_data = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matrix = Matrix(matrix_data)
print("Adjacent numbers to 5:", matrix.get_adjacent(1, 1))