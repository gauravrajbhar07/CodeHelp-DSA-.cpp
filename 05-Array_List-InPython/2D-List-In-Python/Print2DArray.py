matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

row,col = 3 ,3 


matrix =[[1 for i in range(col)] for j in range(row)]
# print(matrix)

for i in range(row):

    # print(i)
    for j in range(col):
        print(matrix[i][j],end="")

    print('\n')


# row, col = 3, 3

# matrix = [[i+1 for i in range(col)] for j in range(row)]

# for i in range(row):
#     for j in range(col):
#         print(matrix[i][j])
#     print('\n')





