<h1 align="center">Ransomware python</h1>
<p align="center"><a href="https://cdn.jsdelivr.net/gh/sindresorhus/awesome@d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg?label=Repo%20size&style=flat-square"> <img src="https://cdn.jsdelivr.net/gh/sindresorhus/awesome@d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg?label=Repo%20size&style=flat-square" alt="Awesome" /></a> <a align="center"><a href="https://api.codacy.com/project/badge/Grade/441b48966e9f4b58a643d7c4cee8ba66?label=Repo%20size&style=flat-square"> <img src="https://api.codacy.com/project/badge/Grade/441b48966e9f4b58a643d7c4cee8ba66?label=Repo%20size&style=flat-square" alt="Repo Size" /></a> <a align="center"><a href="https://img.shields.io/github/repo-size/Sasser1337/Ransomware.svg?label=Repo%20size&style=flat-square"> <img src="https://img.shields.io/github/repo-size/Sasser1337/Ransomware.svg?label=Repo%20size&style=flat-square" alt="Repo Size" /></a></p> </p><p align="center"><a 

<h2 align="center">Simple code to create Ransomware using python</h2>

<p align="center"><a href="https://github.com/Sasser1337/Ransomware/stargazers"><img src="https://img.shields.io/github/stars/Sasser1337/Ransomware" alt="Stars Badge"/></a> <a align="center">
<a href="https://github.com/Sasser1337/awesome-github-profile-readme/network/members"><img src="https://img.shields.io/github/forks/Sasser1337/Ransomware" alt="Forks Badge"/></a> <a align="center">
<a href="https://github.com/Sasser1337/Ransomware/blob/master/LICENSE"><img src="https://img.shields.io/github/license/Sasser1337/Ransomware?color=2b9348" alt="License Badge"/></a> <a align="center">

<h2> You need to change the Ransomware.py code </h2>

```python
# Specify your encryption key here
encryption_key = b'YourEncryptionKey'  # Replace 'Your Encryption Key' with the desired encryption key.

<h2> Also change the message for the README.txt file </h2>

```python
f.write(b'Your message')

<h2> Change the target directory to encrypt files </h2>

```python
# Define the directory path here (replace with your desired directory)
directory = '/path/to/your/directory'  # Replace it '/path/to/your/directory' with the directory path you want to encrypt.

<i>How this code works</i>

<h2> Encryption Part: </h2>

- [The program begins by defining the 'encrypt_files(file_name, key) function, which is used to encrypt a file. It opens the file in binary read mode ('rb') and reads its entire contents.]

- [Next, the program performs XOR operation on each byte of the file using the specified encryption key. This results in the encrypted data.]

- [A new file with the '.encrypted' extension is created to store the encrypted data, and the encrypted data is written to this new file.]

- [The original file is removed to prevent access to the original content.]

- [The program also defines the 'encrypt_all_files(directory, key) function, which is used to encrypt all files in the specified directory. It processes all files in the directory, including those in sub-directories, recursively.]

- [After all files are encrypted, the program creates a 'README.txt' file that contains a specific message or instructions. This is the file that will be used to store the encryption key. The key is not stored in plaintext within the code but must be provided by the user later.]

- [The 'README.txt' file containing the message and encryption key is moved to the same directory as the encrypted files.]

<h2> Decryption Part: </h2>

- [The program defines the decrypt_files(file_name, key) function, which is used to decrypt an encrypted file. It follows the same steps as encryption but uses the decryption key.]

- [The program also defines the decrypt_all_files(directory, key) function, which is used to decrypt all encrypted files in the specified directory.]

<h2> User Interaction: </h2>

- [After all files are encrypted, the program enters a while loop that allows the user to input the decryption key.]

- [The user is prompted to enter the decryption key, and the program checks if the key entered by the user matches the predefined encryption key.]

- [If the key matches, the program proceeds to decrypt the files in the directory using the correct key. If the key does not match, a "Wrong key. Please try again." message is displayed, and the user is prompted to enter the key again.]

- [Once the correct key is entered, the decryption process continues, and the files are restored to their original state.]

