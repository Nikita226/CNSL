#include <iostream>
using namespace std;

string encrypt(string text, int s)
{
	string result = "";
	unsigned int i;
	for (i = 0; i < text.length(); i++) {
		if (isupper(text[i]))
			result += char(int(text[i] + s - 65) % 26 + 65);
		else
			result += char(int(text[i] + s - 97) % 26 + 97);
	}
	return result;
}

string decrypt(string text, int s)
{
	string result = "";
	unsigned int i;
	for (i = 0; i < text.length(); i++) {
		if (isupper(text[i]))
			result += char(int(text[i] - s - 65) % 26 + 65);
		else
			result += char(int(text[i] - s - 97) % 26 + 97);
	}
	return result;
}

int main()
{
	string text;
	cout << "Text : ";
    cin>>text;

	int s;
	cout << "\nShift: ";
    cin>>s;

	string cipher;
	cipher = encrypt(text, s);
	cout << "\nAfter Encrpytion\nCipher: " << cipher;

	cout << "\n\nAfter Decryption\nPlain Text: " << decrypt(cipher, s);
	return 0;
}
