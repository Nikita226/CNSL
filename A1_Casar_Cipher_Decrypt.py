import nltk
nltk.download('words')
from nltk.corpus import words

def caesar_decrypt(ciphertext, shift):
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            decrypted_char = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    
    return decrypted_text

def is_meaningful_word(word):
    return word.lower() in words.words()

def decrypt_with_meaningful_text(ciphertext):
    for shift in range(26):
        decrypted_text = caesar_decrypt(ciphertext, shift)
        print(decrypted_text)
        if all(is_meaningful_word(word) for word in decrypted_text.split()):
            return decrypted_text

encrypted_text = "kgvt"
decrypted_answer = decrypt_with_meaningful_text(encrypted_text)

if decrypted_answer:
    print("\nDecrypted answer:", decrypted_answer, "\n")
else:
    print("No valid decryption found.")