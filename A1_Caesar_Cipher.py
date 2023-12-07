# Caesar Cipher Technique
def encrypt(text,s):
	result = ""
	for i in range(len(text)):
		ch = text[i]
		if (ch.isupper()):
			result += chr((ord(ch) + s - 65) % 26 + 65) # Encrypt uppercase characters
		else:
			result += chr((ord(ch) + s - 97) % 26 + 97) # Encrypt lowercase characters
	return result

def decrypt(text,s):
	result = ""
	for i in range(len(text)):
		ch = text[i]
		if (ch.isupper()):
			result += chr((ord(ch) - s - 65) % 26 + 65) # Decrypt uppercase characters
		else:
			result += chr((ord(ch) - s - 97) % 26 + 97) # Decrypt lowercase characters
	return result


text = input("\nPlain text: ")
s = int(input("Shift: "))
cipher = encrypt(text,s)
print("\nEncrypted Cipher Text: " + cipher)
plain = decrypt(cipher,s)
print("Decrypted Text : " + plain + "\n")