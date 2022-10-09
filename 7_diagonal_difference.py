def diagonalDifference(arr):
    
    left, right = 0, 0
    for i in range(len(arr)):
        left += arr[i][i]
        right += arr[i][len(arr) - i - 1]
    print(abs(left - right))

if __name__ == '__main__':


    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

  

