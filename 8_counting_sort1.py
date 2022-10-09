def countingSort(arr):
    result = [0] * 100
    for i in arr:
        result[i] += 1
    return result


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)



