def reverseList(lst):
    left = 0
    right = len(lst) - 1

    while(left <= right):
        lst[left],lst[right] = lst[right],lst[left]
        left = left + 1
        right = right  - 1

    
def main():
    n = int(input())
    lst = list(map(int,input().split()))
    reverseList(lst)

    print(lst)

if __name__ == "__main__":
    main()


