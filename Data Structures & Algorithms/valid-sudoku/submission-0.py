class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if not board:
            return True

        for row in board: 
            if not self._isValidRow(row):
                return False

        for col in range(len(board[0])):
            input_col = []
            for row in range(len(board)):
                input_col.append(board[row][col])
            if not self._isValidColumn(input_col):
                return False
        
        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                subBox = [board[i][j] for i in range(r, r + 3) for j in range(c, c + 3)]
                if not self._isValidRow(subBox):
                    return False

        
        return True

    def _isValidRow(self, row: List[str]) -> bool:
        count = {}
        for num in row:
            if num == ".":
                continue
            if num in count:
                return False
            else:
                count[num] = 1
        return True

    def _isValidColumn(self, col: List[str]) -> bool:
        count = {}
        for num in col:
            if num == ".":
                continue
            if num in count:
                return False
            else:
                count[num] = 1
        return True
    
    def _isValidSubBox(self, subBox: List[List[str]]) -> bool:
        count = {}
        for i in range(len(subBox)):
            for j in range(len(subBox[0])):
                num = subBox[i][j]
                if num == ".":
                    continue
                if num in count:
                    return False
                else:
                    count[num] = 1
        return True