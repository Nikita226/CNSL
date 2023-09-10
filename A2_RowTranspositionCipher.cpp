// Assignment 2 b)
#include<bits/stdc++.h>
using namespace std;

string encryptMessage(string msg,string const key,map<int,int> keyMap)
{
	int row,col,j;
	string cipher = "";
	
	col = key.length();
	row = msg.length()/col;
	
	if (msg.length() % col)
		row += 1;

	char matrix[row][col];
	for (int i=0,k=0; i < row; i++)
	{
		for (int j=0; j<col; )
		{
			if(msg[k] == '\0')
			{
				matrix[i][j] = '_';	
				j++;
			}
			
			if( isalpha(msg[k]) || msg[k]==' ')
			{
				/* Adding only space and alphabet into matrix*/
				matrix[i][j] = msg[k];
				j++;
			}
			k++;
		}
	}

	for (map<int,int>::iterator ii = keyMap.begin(); ii!=keyMap.end(); ++ii)
	{
		j=ii->second;
		
		// getting cipher text from matrix column wise using permuted key
		for (int i=0; i<row; i++)
		{
			if( isalpha(matrix[i][j]) || matrix[i][j]==' ' || matrix[i][j]=='_')
				cipher += matrix[i][j];
		}
	}

	return cipher;
}

// Decryption
string decryptMessage(string cipher,string const key,map<int,int> keyMap)
{
	int col = key.length();

	int row = cipher.length()/col;
	char cipherMat[row][col];

	for (int j=0,k=0; j<col; j++)
		for (int i=0; i<row; i++)
			cipherMat[i][j] = cipher[k++];
	
	int index = 0;
	for( map<int,int>::iterator ii=keyMap.begin(); ii!=keyMap.end(); ++ii)
		ii->second = index++;

	char decCipher[row][col];
	map<int,int>::iterator ii=keyMap.begin();
	int k = 0;
	for (int l=0,j; key[l]!='\0'; k++)
	{
		j = keyMap[key[l++]];
		for (int i=0; i<row; i++)
		{
			decCipher[i][k]=cipherMat[i][j];
		}
	}

	string msg = "";
	for (int i=0; i<row; i++)
	{
		for(int j=0; j<col; j++)
		{
			if(decCipher[i][j] != '_')
				msg += decCipher[i][j];
		}
	}
	return msg;
}

int main()
{
	string msg = "nikita khot";
    string key = "hack";
    map<int,int> keyMap;

    for(int i=0; i < key.length(); i++)
		keyMap[key[i]] = i;
	
	string cipher = encryptMessage(msg, key, keyMap);
	cout << "Encrypted Message: " << cipher << endl;
	cout << "Decrypted Message: " << decryptMessage(cipher, key, keyMap) << endl;

	return 0;
}