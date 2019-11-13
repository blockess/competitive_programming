class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def get_number_in_cell(location):
            location_indexes = [[0,1,2],[3,4,5],[6,7,8]]
            cell = []
            for i in location_indexes[location//3]:
                    for j in location_indexes[location%3]:
                        if board[i][j].isnumeric():
                            cell.append(board[i][j])
            return cell
        
        def get_number_in_line(location):
            return [c for c in board[location] if c.isnumeric()]
        
        def get_number_in_column(location):
            return [c[location] for c in board if c[location].isnumeric()]
        
        for f in [get_number_in_cell, get_number_in_line, get_number_in_column]:
            for l in range(9):
                numbers = f(l)
                if len(set(numbers)) != len(numbers):
                    return False
        
        return True
