# Validate the given sudoku questionnaire
# example 1
# Input: board = 
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: true

# Example 2:

# Input: board = 
# [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: false
# Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. 
# Since there are two 8's in the top left 3x3 sub-box, it is invalid.

def isValidSudoku(board):
        for i in range(9):
            row=[]
            for j in range(9):
                if not board[i][j]=='.' :
                    if board[i][j] not in row :
                        row.append(board[i][j])
                    else:
                        return False
                col=[]
                for k in range(9):
                    if not board[k][j]=='.':
                        if board[k][j] not in col:
                            col.append(board[k][j])
                        else:
                            return False
        for i in range(3):
            for l in range(3):
                box=[]
                
                for j in range(i*3,(i+1)*3):
                    for k in range(l*3,(l+1)*3):
                        if not board[j][k]=='.':
                            if board[j][k] not in box:
                                box.append(board[j][k])
                            else:
                                return False
                        
        return True

board=[]

for i in range(9):
    tem=[]
    print('enter ',i,'th row 9 valuse by seprating with commas to leave spaces enter fullstop: ')
    tem =list(map(str,input().split(',')))
    board.append(tem)

print(isValidSudoku(board))