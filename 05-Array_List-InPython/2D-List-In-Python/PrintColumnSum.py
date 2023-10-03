def printColSum(alist):

# 11 24 23 22
    row = len(alist)
    col = len(alist[0])
    print("hello")
    for i in range(col):
        sum_val = 0 
        for j in range(row):
            sum_val = sum_val + alist[j][i]
        print(sum_val, end=" ")
            

def main():

    alist = [[1,2,3,4],
             [2,3,4,1],
             [5,6,1,3],
             [2,4,6,8],
             [1,9,9,6]
            ]
    printColSum(alist)


if __name__ == "__main__":
    main() 