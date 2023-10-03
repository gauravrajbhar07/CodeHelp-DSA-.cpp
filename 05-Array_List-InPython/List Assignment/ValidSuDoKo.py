# https://leetcode.com/problems/valid-sudoku/description/

'''
Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
Example 2:

Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
 

'''

from collections import defaultdict

def checkRow(board):
    #condition One row 
    row = len(board)
    col = len(board[0])
    
    
    for i in range(row):
        hset = set()
        for j in range(col):
            # print(board[i][j],end=" ")
            if(board[i][j] == "."):
                # print(board[k][j], val)
                pass
            elif(board[i][j] in hset):
                # print(hset,board[i][j],end=' ')
                return False
            else:
                hset.add(board[i][j])
        
                
    return True
                
            
    
    
def checkCol(board):
    #condition One row 
    row = len(board)
    col = len(board[0])
    
    
    for i in range(col):
        hset = set()
        for j in range(row):
            # print(board[j][i],end=" ")
            if(board[j][i] == "."):
                # print(board[k][j], val)
                pass
            elif(board[j][i] in hset):
                # print(hset,board[j][i],end=' ')
                return False
            else:
                hset.add(board[j][i])
        if(len(hset) == 0):
            return True
                
    return True


def Check3X3(board):
    
    squares = defaultdict(set) #key = (r//3 ,c//3)
        # emptyset = set()
        # for i in range(9):
        #     for j in range(9):
        #         emptyset.add(board[i][j])
        # # print(emptyset)
        # if(len(emptyset) == 1):
        #     return True
        

    for i in range(9):

        for j in range(9):
                # print(board[j][i],end=" ")
            if(board[i][j] == "."):
                    # print(board[k][j], val)
                  pass
            elif(board[i][j] in squares[(i//3 ,j//3)]):
                    # print(hset,board[j][i],end=' ')
                 return False
            else:
                    squares[(i//3 ,j//3)].add(board[i][j])
    print(squares)
            
        
        
    return True
    
    # squares = defaultdict(set) #key = (r//3 ,c//3)
    # # emptyset = set()
    # # for i in range(9):
    # #     for j in range(9):
    # #         emptyset.add(board[i][j])
    # # # print(emptyset)
    # # if(len(emptyset) == 1):
    # #     return True
    

    # for i in range(9):
   
    #     for j in range(9):
    #         # print(board[j][i],end=" ")
    #         if(board[i][j] == "."):
    #             # print(board[k][j], val)
    #             pass
    #         elif(board[i][j] in squares[(i//3 ,j//3)]):
    #             # print(hset,board[j][i],end=' ')
    #             return False
    #         else:
    #             squares(i//3 ,j//3).add(board[i][j])
        
    # return True





def ValidSuDoKo(board):
    
    #condition One row 
    chR = checkRow(board)
    
    chC = checkCol(board)
    
    chB = Check3X3(board)
    # print(chR,chB,chC)
    
    if(chR ==True and chC == True and chB == True):
        return True
    else:
        return False
    
    
    
                
    
    
    






# board = [["8","3",".",".","7",".",".",".","."]
#         ,["6",".",".","1","9","5",".",".","."]
#         ,[".","9","8",".",".",".",".","6","."]
#         ,["8",".",".",".","6",".",".",".","3"]
#         ,["4",".",".","8",".","3",".",".","1"]
#         ,["7",".",".",".","2",".",".",".","6"]
#         ,[".","6",".",".",".",".","2","8","."]
#         ,[".",".",".","4","1","9",".",".","5"]
#         ,[".",".",".",".","8",".",".","7","9"]]

# board = [["8",".",".",".","6",".",".",".","3"]
#         ,["4",".",".","8",".","3",".",".","1"]
#         ,["7",".",".",".","2",".",".",".","6"]
#         ,[".","6",".",".",".",".","2","8","."]
#         ,[".",".",".","4","1","9",".",".","5"]
#         ,[".",".",".",".","8",".",".","7","9"]
#         ,[".",".",".",".","7",".",".",".","."]
#         ,[".",".",".","1","9","5",".",".","."]
#         ,[".",".",".",".",".",".",".","6","."]]

# board = [["8","3",".",".","7",".",".",".","."],
#         ["6",".",".","1","9","5",".",".","."],
#         [".","9","8",".",".",".",".","6","."],
#         ["8",".",".",".","6",".",".",".","3"],
#         ["4",".",".","8",".","3",".",".","1"],
#         ["7",".",".",".","2",".",".",".","6"],
#         [".","6",".",".",".",".","2","8","."],
#         [".",".",".","4","1","9",".",".","5"],
#         [".",".",".",".","8",".",".","7","9"]]


# board = [[".",".",".",".",".",".",".",".","."],
#          [".",".",".",".",".",".",".",".","."],
#          [".",".",".",".",".",".",".",".","."],
#          [".",".",".",".",".",".",".",".","."],
#          [".",".",".",".",".",".",".",".","."],
#          [".",".",".",".",".",".",".",".","."],
#          [".",".",".",".",".",".",".",".","."],
#          [".",".",".",".",".",".",".",".","."],
#          [".",".",".",".",".",".",".",".","."]]

board =[[".",".","5",".",".",".",".",".","6"],
        [".",".",".",".","1","4",".",".","."],
        [".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".","9","2",".","."],
        ["5",".",".",".",".","2",".",".","."],
        [".",".",".",".",".",".",".","3","."],
        [".",".",".","5","4",".",".",".","."],
        ["3",".",".",".",".",".","4","2","."],
        [".",".",".","2","7",".","6",".","."]]
    
print(ValidSuDoKo(board))

# print(Check3X3(board))