import hashlib
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

myStr = 'abcde'
salt = '12345'
prep_salt = str(myStr + salt).encode('utf-8')
myHash = hashlib.sha512(prep_salt).hexdigest()
print(myHash)
mymsg = [prep_salt, myHash]

key = get_random_bytes(16)
cipher = AES.new(key, AES.MODE_EAX)
nonce = cipher.nonce
ciphertext, tag = cipher.encrypt_and_digest(prep_salt)

with open('cipher', 'wb') as cw:
    cw.write(str(len(ciphertext)).encode('utf-8'))
    cw.write(str(len(tag)).encode('utf-8'))
    cw.write(ciphertext)
    cw.write(tag)


with open('cipher', 'rb') as cr:
    ln_cipher = int(cr.read(2))
    ln_tag = int(cr.read(2))
    ciphertext = cr.read(ln_cipher)
    tag = cr.read(ln_tag)

    print("Alice set (ciphertext, tag) to Bob.")
    print("Bob received (ciphertext, tag) from Alice")
    print("Assume that Bob has key (", key, ")")
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt((ciphertext))

    try:
        cipher.verify(tag)
        print("The message (", plaintext, ") is authentic.")
    except ValueError:
        print("Key incorrect or message corrupted")