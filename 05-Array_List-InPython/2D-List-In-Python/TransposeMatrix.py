def TransposeMatrix(alist):


# 11 24 23 22
    row = len(alist)
    col = len(alist[0])

    save = [[0 for i in range(row)] for j in range(col)]
    print(save)

    

    for i in range(row):
        for j in range(col):
            save[i][j] = alist[i][j]

    print(save)

    for i in range(row):
        for j in range(col):
            alist[j][i] = save[i][j]

    print(alist)


        
            
            

def main():

    alist = [[1,2,3,4],
             [2,3,4,1],
             [5,6,1,3],
             [2,4,6,8],
            ]
    TransposeMatrix(alist)


if __name__ == "__main__":
    main() 