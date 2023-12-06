import base64
import binascii

sha1 = "3C0BAA6855FD9B5B5F16B48365CBE972D1F1B5D1"  # SHA1 fingerprint without colons
key_hash = base64.b64encode(binascii.a2b_hex(sha1))
print(key_hash.decode())
