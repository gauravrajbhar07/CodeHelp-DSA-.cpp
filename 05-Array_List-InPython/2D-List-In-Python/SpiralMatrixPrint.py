def spiral(alist):
    res =[]
    left = 0
    right = len(alist)
    top = 0
    bottom = len(alist[0])

    # print(top,left)0 0
    # print(top,right)0 4
    # print(bottom,left)4 0
    # print(bottom,right)4 4

    while(left < right and top < bottom):

        # left to right
        for i in range(left,right):
            res.append(alist[top][i])
        top+=1

        # top to bottom
        for i in range(top,bottom):
            res.append(alist[i][right-1])
        right-=1

        # right to left
        for i in range(right-1,left-1,-1):
            res.append(alist[bottom-1][i])
        bottom-=1

        # bottom to top
        for i in range(bottom-1,top-1,-1):
            res.append(alist[i][left])
        left+=1

    return res




    


# Input:  { {1,    2,   3,   4},
#           {5,    6,   7,   8},
#           {9,   10,  11,  12},
#           {13,  14,  15,  16 }}
# Output: 1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10 



alist =  [[1,    2,   3,   4],
          [5,    6,   7,   8],
          [9,   10,  11,  12],
          [13,  14,  15,  16 ]]

print(spiral(alist))

# [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]
