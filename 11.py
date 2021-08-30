import hashlib


crypto_=hashlib.md5()
crypto_.update(b"hello world")

print(crypto_.hexdigest())

