def countAndSay(n):
    s0 = '1'
    for i in range(1, n):
        s1, k = '', 1
        for j in range(1, len(s0)):
            if s0[j-1] == s0[j]: k += 1
            else: s1, k = s1 + str(k) + s0[j-1], 1
        s1 += str(k) + s0[-1]
        s0 = s1
    return s0

print(countAndSay(6))