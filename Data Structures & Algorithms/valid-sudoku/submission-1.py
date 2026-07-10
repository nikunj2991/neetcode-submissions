class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if not board:
            return True
        
        seen = set()

        for row in range(9):
            for col in range(9):
                val = board[row][col]
                if val == ".":
                    continue
                
                rowStr = f"{val} in row {row}"
                colStr = f"{val} in col {col}"
                boxStr = f"{val} in box {row // 3} {col //3}"

                if (rowStr in seen) or (colStr in seen) or (boxStr in seen):
                    return False
                
                seen.add(rowStr)
                seen.add(colStr)
                seen.add(boxStr)
        
        return True