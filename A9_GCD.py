import pandas as pd
def main():
    a = int(input("\nEnter 1st number : "))
    b = int(input("Enter 2nd number : "))
    Q, R1, R2, R = [], [], [], []
    r1, r2 = a, b
    while r2 > 0:
        q = r1 // r2
        r = r1 - q * r2
        r1, r2 = r2, r

        Q.append(q)
        R.append(r)
        R1.append(r1)
        R2.append(r2)
    
    df = pd.DataFrame({"q": Q, "r1": R1, "r2" : R2, "r" : R})
    print(df)
    print()
    print(f"GCD({a}, {b}) = {r1}")
    print()

if __name__ == "__main__":
    main()