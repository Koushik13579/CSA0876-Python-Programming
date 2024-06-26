def myPow(x, n):
    def fastPow(x, n):
        if n == 0:
            return 1.0
        half = fastPow(x, n // 2)
        if n % 2 == 0:
            return half * half
        else:
            return half * half * x

    if n < 0:
        x = 1 / x
        n = -n
    return fastPow(x, n)
x = 2.00000
n = 10
print("Output for Test Case 1:", myPow(x, n)) 
