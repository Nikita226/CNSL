import sympy

def find_factor_pairs(n):
    factor_pairs = []
    ans = False
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            pair = (i, n // i)
            if sympy.isprime(i) and sympy.isprime(n // i):
                factor_pairs.append(pair)
                ans = True
    if ans == False:
        print("No prime factors")
    return factor_pairs

def display_factorization_pairs(n):
    factor_pairs = find_factor_pairs(n)
    for pair in factor_pairs:
        print(f"{n} = {pair[0]} * {pair[1]}")

if __name__ == "__main__":
    number = int(input("\nEnter the number: "))
    display_factorization_pairs(number)
    print()

