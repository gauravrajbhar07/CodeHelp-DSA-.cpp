def find132pattern(nums):
        a = 0 
        b = 1
        c = 2
        size = len(nums)
        flag = 0
        while(c<=size or a <= size or c <= size):
            if(a<c and a<b and b>c):
                print("hello")
                flag = 1
                break
            print(a,b,c)
            a+=1
            b+=1
            c+=1
        if(flag == 1):
            return True
        else:
            return False
        
        
print(find132pattern([3,1,4,2]))