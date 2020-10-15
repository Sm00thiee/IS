import a51
import sys


key = str(a51.user_input_key())
a51.set_key(key)
first_choice = a51.user_input_choice()
if(first_choice == '0'):
	sys.exit(0)
elif(first_choice == '1'):
	plaintext = str(a51.user_input_plaintext())
	print(plaintext)
	print(a51.encrypt(plaintext))
elif(first_choice == '2'):
	ciphertext = str(a51.user_input_ciphertext())
	print(a51.decrypt(ciphertext))	