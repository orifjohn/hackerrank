def plusMinus(arr):
    positive = [a for j, a in enumerate(arr) if a>0]
    negative = [a for j, a in enumerate(arr) if a<0]
    zero = [a for j, a in enumerate(arr) if a == 0]
    
    positive_values = len(positive) / len(arr)
    negative_values = len(negative) / len(arr)
    zero_values = len(zero) / len(arr)
    
    print("{:.6f}".format(positive_values))
    print("{:.6f}".format(negative_values))
    print("{:.6f}".format(zero_values))
    
if __name__ == '__main__':
    n = int(input().strip())
    
    arr = list(map(int, input().rstrip().split()))
    
    plusMinus(arr)
