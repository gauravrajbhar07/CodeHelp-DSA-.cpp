'''
Input: mat[][] ={{ 1,2,3,4}
                {5,6,7,8}
                {9, 10, 11, 12}
                {13, 14, 15, 16}
                {17, 18, 19, 20}}
Output: 1 5 9 13 17 18 14 10 6 2 3 7 11 15 19 20 16 12 8 4 
'''

def WavePrin(alist):

    row = len(alist)
    col = len(alist[0])
    res=[]
    for i in range(col):

        if(i %2 == 0):
            for j in range(row):
                res.append(alist[j][i])
        
        else:
            for j in range(row-1,-1,-1):
                res.append(alist[j][i])


    print(res)


alist = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16], [17, 18, 19, 20]]
 
WavePrint(alist)
