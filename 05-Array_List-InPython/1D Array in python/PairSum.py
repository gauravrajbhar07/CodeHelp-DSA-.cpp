# //i/p
# // 7       
# // 1 3 5 7 2 4 6
# // 9

# //o/p
# // 3 6
# // 5 4
# // 7 2

def PairSum(arr, sum_val):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == sum_val:
                print(arr[i], arr[j])

def main():
    n = int(input())
    # arr = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    sum_val = int(input())

    PairSum(arr, sum_val)

if __name__ == "__main__":
    main()
