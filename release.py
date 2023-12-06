import base64
import binascii

sha1 = "A0B65552880014C32F517574F47AC75D528AFDAB"  # SHA1 fingerprint without colons
key_hash = base64.b64encode(binascii.a2b_hex(sha1))
print(key_hash.decode())
