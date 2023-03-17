#include <iostream>
#include <fstream>
#define BYTE_SIZE 16

using namespace std;
int* generator_RC4(int byte_length, int* key, size_t key_length)
{
	int* result = new int[byte_length];
	int s[256];
	for (size_t i = 0; i < 256; i++)
	{
		s[i] = i;
	}
	size_t j = 0;
	for (size_t i = 0; i < 256; i++)
	{
		j = (j + s[i] + key[i % key_length]) % 256;
		swap(s[i], s[j]);
	}
	int i = 0;
	j = 0;
	for (size_t k = 0; k < byte_length; k++)
	{
		i = (i + 1) % 256;
		j = (j + s[i]) % 256;
		swap(s[i], s[j]);
		result[k] = s[(s[i] + s[j]) % 256];
	}
	return result;
}
void write_key(string filename, int* key, size_t length)
{
	ofstream out(filename);
	if (out.is_open())
	{
		for (size_t i = 0; i < length; i++)
		{
			out << key[i] << " ";
		}
	}
	out.close();
}
void read_key(string filename, int* when)
{
	int value;
	ifstream in(filename);
	if (in.is_open())
	{
		size_t i = 0;
		while (in >> value)
		{
			when[i++] = value;
		}
	}
	in.close();
}
void to_binary(string filename, int* key, size_t length)
{
	ofstream out(filename);
	if (out.is_open())
	{
		for (size_t i = 0; i < length; i++)
		{
			string s;
			int x = key[i];
			for (size_t j = 0; j < 8; j++)
			{
				s = s + static_cast<char>(x % 2 + '0');
				x = x / 2;
			}
			reverse(s.begin(), s.end());
			out << s;
		}
	}
	out.close();
}
int main()
{
	int key[BYTE_SIZE];
	read_key("key.txt", key);
	int* new_key = generator_RC4(BYTE_SIZE, key, BYTE_SIZE);
	to_binary("subsequence.txt", new_key, BYTE_SIZE);
	write_key("key.txt", new_key, BYTE_SIZE);
	delete[] new_key;
	return 0;
}