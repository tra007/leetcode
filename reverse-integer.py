def reverseNumber(x) -> int:
    if abs(x) < 2**31 and x != 2**31 - 1:
        if x >= 0:
            x=str(x)
            number=int(x[::-1])
        else:
            x=str(x)
            a=x[::-1]
            number=x[0]+a[:-1]
        return int(number)
    return 0


print(reverseNumber((30)))
