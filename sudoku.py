
class Solution:
    def isValidSudoku(self, board) -> bool:
        self.input = board
        return self.validateInput() and self.isValidRow() and self.isValidColumn() and self.isValidMatrix()

    def validateInput(self):
        print(isinstance(self.input, list))
        
        if isinstance(self.input, list) and len(self.input) == 9:
            for rowNumber, row in enumerate(self.input):
                if len(row) != 9:
                    return False
                for position, value in enumerate(row):
                    if not (value.isdigit() or value == "."):
                        return False
            return True
        return False

    def isValidRow(self):
        for row in self.input:
            numbers = []
            for element in row:
                if element != ".":
                    numbers.append(element)
            if sorted(numbers) != sorted(list(set(numbers))):
                return False
        return True

    def isValidColumn(self):
        for row in range(9):
            numbers = []
            for column in range(9):
                if self.input[column][row] != ".":
                    numbers.append(self.input[column][row])
            if sorted(numbers) != sorted(list(set(numbers))):
                return False
        return True

    def isValidMatrix(self):
        for col in range(3):
            for row in range(0, 9, 3):
                numbers = []
                colIndex = list(range(9)[row:row + 3])
                for rowIndex in range(3):
                    for i in range(3):
                        if self.input[rowIndex + (col * 3)][colIndex[i]] != '.':
                            numbers.append(self.input[rowIndex + (col * 3)][colIndex[i]])
                if sorted(numbers) != sorted(list(set(numbers))):
                    return False
        return True


sol = Solution()
print(sol.isValidSudoku(board=[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))
