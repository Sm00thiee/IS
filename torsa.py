import rsa

message = b"This is the message to be encrypted"
public_key, private_key = rsa.newkeys(1024)
encrypted_message = rsa.encrypt(message, public_key)
decrypted_message = rsa.decrypt(encrypted_message, private_key)
print(encrypted_message, decrypted_message, sep="\n\n")