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
    # Check if g is a primitive root modulo p
    values = set()
    for i in range(1, p):
        values.add(pow(g, i, p))
        if len(values) == p - 1:
            return True
    return False
for candidate in range(2, q):
    if is_primitive_root(candidate, q):
        a=candidate
print(f"Prime Number:{q}")
print(f"Primitive Root:{a}")
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("192.168.164.106", 8888))
server.listen(1)

print("Waiting for incoming connections...")
client, addr = server.accept()
print(f"Connection from {addr}")

private_key = random.randint(1, q - 1)
public_key = mod_pow(a, private_key, q)

client.send(str(public_key).encode())
client_public_key = int(client.recv(1024).decode())
print(f"Public key of Client:{client_public_key}")
shared_secret = mod_pow(client_public_key, private_key, q)

print(f"Shared Secret Key: {shared_secret}")

client.close()
server.close()