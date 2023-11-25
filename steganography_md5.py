import cv2
import os
import hashlib
import requests

def encryptstringmd5(input_string):
    try:
        hash_object = hashlib.md5()
        hash_object.update(input_string.encode('utf-8'))
        md5_hash = hash_object.hexdigest()
        return md5_hash
    except Exception as e:
        print("Error: " + str(e))
        
def decode_hash(input_string):
    url = f"https://md5decrypt.net/en/Api/api.php?hash={input_string}&hash_type={'md5'}&email={'yacavim668@newnime.com'}&code={'fdb56e901f303c4d'}"
    response=requests.get(url)
    return response.text

img=cv2.imread(input("enter image file directory : "))
msg=input("enter the secret msg : ")
encryptedmsg=encryptstringmd5(msg)
password=input("enter the encoding password :")

d={}
c={}
for i in range(255):
   d[chr(i)]=i
   c[i]=chr(i)

m=0
n=0
z=0

for i in range(len(encryptedmsg)):
    img[n,m,z]=d[encryptedmsg[i]]
    n+=1
    m+=1
    z=(z+1)%3
    

cv2.imwrite("encryptedimage.jpg",img)
os.startfile("encryptedimage.jpg")

decpryptEncryptedMessage=""

m=0
n=0
z=0

pas=input("enter the decrypting password: ")


if(password==pas):
    
    for i in range(len(encryptedmsg)):
        decpryptEncryptedMessage=decpryptEncryptedMessage+c[img[n,m,z]]
        n+=1
        m+=1
        z=(z+1)%3
    print("Decrypted message is : ",decode_hash(decpryptEncryptedMessage))
else:
    print("invalid password")