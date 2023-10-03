import sys

print(sys.maxsize)


def FindMaxAndMinIn2DList(alist):

    ans = []
    row = len(alist)
    col = len(alist[0])

    min  = sys.maxsize
    max = -sys.maxsize - 1


    for i in range(row):
        for j in range(col):
            if(alist[i][j] > max):
                max = alist[i][j]
    
    ans.append(max)

    for i in range(row):
        for j in range(col):
            if(alist[i][j] < min):
                min = alist[i][j]
    
    ans.append(min)


    return ans





    
    

def main():

    alist = [[1,2,3,4],[2,3,4,1],[5,6,1,3],[2,4,6,8],[1,9,9,6]]
    print(FindMaxAndMinIn2DList(alist))
    


if __name__ == "__main__":
    main()