import socket
import random

q = 23

def mod_pow(base, exponent, modulus):
    if modulus == 1:
        return 0
    result = 1
    base = base % modulus
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        base = (base * base) % modulus
        exponent = exponent // 2
    return result

def is_primitive_root(g, p):
    values = set()
    for i in range(1, p):
        values.add(pow(g, i, p))
        if len(values) == p - 1:
            return True
    return False

for candidate in range(2, q):
    if is_primitive_root(candidate, q):
        a=candidate

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client.connect(("192.168.164.1", 8888))
client.connect(("192.168.153.96", 8888))
server_public_key = int(client.recv(1024).decode())

private_key = random.randint(1, q - 1)
public_key = mod_pow(a, private_key, q)

client.send(str(public_key).encode())

shared_secret = mod_pow(server_public_key, private_key, q)

print(f"Prime Number : {q}")
print(f"Primitive root : {a}")
print(f"Public key of server : {server_public_key}")
print(f"Shared Secret Key: {shared_secret}")


client.close()
