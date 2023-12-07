// Rail Fence Cipher
#include <bits/stdc++.h>
using namespace std;

string encryptRailFence(string text, int key)
{
	char rail[key][(text.length())];
	int i, j;
	for (i=0; i < key; i++)
	{
		for (j = 0; j < text.length(); j++)
			rail[i][j] = '\n';
	}
	bool dir_down = false;
	int row = 0, col = 0;
	for (i=0; i < text.length(); i++)
	{
		if (row == 0 || row == key-1)
			dir_down = !dir_down;
		rail[row][col++] = text[i];
		dir_down ? row++ : row--;
	}
	string result;
	for (i=0; i < key; i++)
	{
		for (j=0; j < text.length(); j++)
		{
			if (rail[i][j]!='\n')
			{
				result.push_back(rail[i][j]);
				cout << rail[i][j];
			}
			else
				cout << " ";
			cout << " "; 
		}
		cout << "\n";
	}
	return result;
}

string decryptRailFence(string cipher, int key)
{
	char rail[key][cipher.length()];
	int i, j;
	for (i=0; i < key; i++)
		for (j=0; j < cipher.length(); j++)
			rail[i][j] = '\n';
	bool dir_down;
	int row = 0, col = 0;
	for (i=0; i < cipher.length(); i++)
	{
		if (row == 0)
			dir_down = true;
		if (row == key-1)
			dir_down = false;
		rail[row][col++] = '*';
		dir_down?row++ : row--;
	}
	int index = 0;
	for (i=0; i<key; i++)
		for (j=0; j<cipher.length(); j++)
			if (rail[i][j] == '*' && index<cipher.length())
				rail[i][j] = cipher[index++];
	string result;

	row = 0, col = 0;
	for (i=0; i< cipher.length(); i++)
	{
		if (row == 0)
			dir_down = true;
		if (row == key-1)
			dir_down = false;
		result.push_back(rail[row][col++]);
		dir_down?row++: row--;
	}
	return result;
}

int main()
{
	string plain_text;
	cout << "\nPlain Text: ";
	cin >> plain_text;
	int key = 3;
	cout << "Key: ";
	cin >> key;
	string cipher_text, decrypted_text;
	cipher_text = encryptRailFence(plain_text, key);
	cout << "\nEncrypted Text: " << cipher_text << endl;
	decrypted_text = decryptRailFence(cipher_text, key);
	cout << "Decrypted Test: " << decrypted_text << "\n\n";
	return 0;
}