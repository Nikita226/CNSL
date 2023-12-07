import pandas as pd
def euclidean_algo(a, b):
    s1, s2, s, t1, t2, t = 1, 0, 0, 0, 1, 0
    r1, r2 = a, b
    Q, R1, R2, R, T1, T2, T, S, S1, S2 = [], [], [], [], [], [], [], [], [], []
    while r2 > 0:
        q = r1 // r2
        r = r1 - q * r2
        t = t1 - q * t2
        s = s1 - q * s2

        Q.append(q)
        R.append(r)
        R1.append(r1)
        R2.append(r2)
        T.append(t)
        T1.append(t1)
        T2.append(t2)
        S.append(s)
        S1.append(s1)
        S2.append(s2)
        r1 = r2
        r2 = r
        s1 = s2
        s2 = s
        t1 = t2
        t2 = t

    df = pd.DataFrame({"q": Q, "r1": R1, "r2" : R2, "r" : R, "S1" : S1, "S2" : S2 , "S" : S,"T1" : T1, "T2" : T2, "T" : T})
    print(df)
    print()
    res = -1
    if r1 == 1:
        res = t1
    return res

def main():
    a = int(input("Enter number a : "))
    b = int(input("Enter number b : "))

    print()

    ans = float('inf')
    if b > a:
        ans = euclidean_algo(b, a)
    else:
        ans = euclidean_algo(a, b)

    if ans != -1:
        print(f"Multiplicative inverse of {b} in {a} : {ans}", end='')
        if ans < 0:
            if b > a:
                ans += b
            else:
                ans += a
            print(f" and {ans}")
        else:
            print()
    else:
        print("Multiplicative inverse is not present.")

if __name__ == "__main__":
    main()
