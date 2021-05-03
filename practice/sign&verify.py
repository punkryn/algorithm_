from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

AlicePrivKey = RSA.generate(2048)

with open('AlicePrivKey.pem', 'wb') as fa:
    fa.write(AlicePrivKey.export_key('PEM', passphrase="!@#$"))

with open('AlicePubKey.pem', 'wb') as apk:
    apk.write(AlicePrivKey.publickey().export_key('PEM'))

BobPrivKey = RSA.generate(2048)
with open('BobPrivKey.pem', 'wb') as bk:
    bk.write(BobPrivKey.export_key('PEM', passphrase="!@#$"))

with open("BobPubKey.pem", 'wb') as bpk:
    bpk.write(BobPrivKey.publickey().export_key('PEM'))

with open("AlicePrivKey.pem", 'r') as akr:
    AlicePrivKey = RSA.import_key(akr.read(), passphrase="!@#$")

message = "get signed"
h = SHA256.new(message.encode('utf-8'))
signature = pkcs1_15.new(AlicePrivKey).sign(h)
print("Alice sent (", message, signature, ") to Bob.")

AlicePubKey = None
with open("AlicePubKey.pem", 'r') as apkr:
    AlicePubKey = RSA.import_key(apkr.read())

print("Bob received message (", message, signature, ") from Alice")
h = SHA256.new(message.encode('utf-8'))

try:
    pkcs1_15.new(AlicePubKey).verify(h, signature)
    print("The signature is valid")
except(ValueError, TypeError):
    print("The signature is not valid")