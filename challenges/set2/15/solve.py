import sage

print("ICE ICE BABY\x04\x04\x04\x04", True, sage.verify_pkcs7(b"ICE ICE BABY\x04\x04\x04\x04"))
print("ICE ICE BABY\x05\x05\x05\x05", False, sage.verify_pkcs7(b"ICE ICE BABY\x05\x05\x05\x05"))
print("ICE ICE BABY\x01\x02\x03\x04", False, sage.verify_pkcs7(b"ICE ICE BABY\x01\x02\x03\x04"))