import numpy as np

board_dict = {}

def create_board_key(board):
    strg = ''
    for i in range(board.shape[0]):
        for j in range(board.shape[1]):
            strg += str(board[i][j])
    return strg

def is_board_safe(board):
    board_key = create_board_key(board)
    if board_key in board_dict:
        return board_dict[board_key]
    row_sum = np.sum(board,axis= 1)
    if len(row_sum[np.where(row_sum > 1)]) > 0:
        board_dict[board_key] = 0
        return 0
    
    col_sum = np.sum(board,axis = 0)
    if len(col_sum[np.where(col_sum > 1)]) > 0:
        board_dict[board_key] = 0
        return 0
    
    diags = [board[::-1,:].diagonal(i) for i in range(-board.shape[0]+1,board.shape[1])]
    #print("left lower to right upper", diags)
    diags.extend([board.diagonal(i) for i in range(board.shape[1]-1,-board.shape[0],-1)])    
    #print("left upper to right lower", diags)
    for diag in diags:
        #print(diag)
        if np.sum(diag) > 1:
            board_dict[board_key] = 0
            return 0
    
    board_dict[board_key] = 1        
    return 1

n = int(input())
board = np.zeros((n,n),int)
#board[0][1] =1
#print(board.shape[0],board.shape[1])
#print(create_board_key(board))

#board[1][1] = 1
#board[2][2] = 1

#print(is_board_safe(board))


def place_queens(board,col):
    if col >= n:
        return True
    for r in range(0,n):
        place = False
        board[r][col] = 1
        if is_board_safe(board):
           place= place_queens(board,col+1)
            
        if not place:
            board[r][col] = 0
        else:
            return True
    return False

if not place_queens(board,0):
    print("NO")
else:
    print("YES")
    print(board)
