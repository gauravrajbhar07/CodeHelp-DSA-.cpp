def findKey(alist ,key):

    row = len(alist)
    col = len(alist[0])

    for i in range(row):
        for j in range(col):
            if(key == alist[i][j]):
                return True
    
    return False




def main():
    key = 5
    alist = [[1,2,3,4],[2,3,4,1],[5,6,1,3],[2,4,6,8],[1,9,9,6]]
    print(findKey(alist,key))

if __name__ == "__main__":
    main()