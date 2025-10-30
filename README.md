# encrypt

XOR Cipher

Description

This is a simple program that encrypts and decrypts text using the XOR (exclusive OR) operation. The program generates a random key of 0s and 1s with the same length as the text. Each character of the text is combined with the corresponding bit of the key using XOR to produce the encrypted text. The same key is then used to decrypt the text and recover the original message.
How It Works

The user inputs a text string.
A random key of 0s and 1s is generated automatically.
Each character of the text is XORed with the corresponding bit of the key to produce the encrypted text.
The encrypted text is XORed again with the same key to recover the original text.
Usage

Run xor_cipher.py with Python 3.
Enter the text you want to encrypt.
The program will display:
The randomly generated key
The encrypted text
The decrypted text

Requirements
Python 3.x
Built-in random module
