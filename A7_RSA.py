import math

def prime_checker(p):
	# Checks If the number entered is a Prime Number or not
	if p < 1:
		return -1
	elif p > 1:
		if p == 2:
			return 1
		for i in range(2, p):
			if p % i == 0:
				return -1
		return 1

def RSA(p: int, q: int, message: int):
    n = p * q
    t = (p - 1) * (q - 1)
    # selecting public key, e
    for i in range(2, t):
        if math.gcd(i, t) == 1:
            e = i
            break
    # selecting private key, d
    j = 0
    while True:
        if (j * e) % t == 1:
            d = j
            break
        j += 1
	
    # performing encryption
    print(f"\nPublic Key <{e}, {n}>")
    ct = (message ** e) % n
    print(f"Encrypted message is {ct}")
	
    # performing decryption
    print(f"\nPrivate Key <{d}, {n}>")
    mes = (ct ** d) % n
    print(f"Decrypted message is {mes}\n")


# Testcase - 1
# RSA(p=53, q=59, message=89)
# # Testcase - 2
# RSA(p=3, q=7, message=12)

while 1:
	p = int(input("\nEnter P : "))
	if prime_checker(p) == -1:
		print("Number Is Not Prime, Please Enter Again!")
		continue
	break

while 1:
	q = int(input("Enter Q : "))
	if prime_checker(q) == -1:
		print("Number Is Not Prime, Please Enter Again!")
		continue
	break

msg = int(input("msg : "))
RSA(p, q, msg)