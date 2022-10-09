def flippingBits(n):
    result = ''
    while n != 0:
        digit = n % 2
        result += str(digit)
        n //= 2
    prefix = ''
    result = result[::-1]
    if len(result) < 32:
        for i in range(32-len(result)):
            prefix += "0"
    prefix = prefix + result

    flipped = ''
    for i in prefix:
        if i == "0":
            flipped += "1"
        else:
            flipped += "0"
    flipped = int(flipped)
    decimal, i = 0, 0

    while (flipped != 0):
        dec = flipped % 10
        decimal = decimal + dec * pow(2, i)
        flipped = flipped // 10
        i += 1

    print(decimal)

if __name__ == '__main__':
   

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = flippingBits(n)

