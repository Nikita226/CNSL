import math

def check_coprime(m):
    n = len(m)
    for i in range(n):
        for j in range(i+1, n):
            if math.gcd(m[i], m[j]) != 1:
                return True
    return False

def CRT(a, m, n):
    x = [0] * n
    M = 1

    for i in range(n):
        M *= m[i]

    for i in range(n):
        r1 = m[i]
        r2 = M // m[i]
        t1, t2 = 0, 1

        while r2 > 0:
            q = r1 // r2
            r = r1 - q * r2
            r1, r2 = r2, r
            
            t = t1 - q * r2
            t1, t2 = t2, t
        if r1 == 1:
            x[i] = t1
        if x[i] < 0:
            x[i] += m[i]

    res = 0
    for i in range(n):
        res += (a[i] * x[i] * M) // m[i]
    
    ans = res % M
    return ans


n = int(input("\nEnter size: "))
a = []
m = []

print("\nEnter values of a:")
for i in range(n):
    a_i = int(input())
    a.append(a_i)

print("\nEnter values of m:")
for i in range(n):
    m_i = int(input())
    m.append(m_i)

print()

for i in range(n):
    print(f'X = {a[i]} mod ({m[i]}) ')

if not check_coprime(m):
    result = CRT(a, m, n)
    print(f"\nValue of X: {result}\n")
else:
    print("\nAs values of m are not coprime, the solution does not exist!\n")
