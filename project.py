#encryption
def encrypt(s):
    string = ""
    binaryConv = []
    for c in s:
        asciiValue = int(ord(c)) + 1        #adding 1 to ascii value
        binaryValue = bin(asciiValue)
        binaryValue = binaryValue[2:]
        if len(binaryValue) == 6:
            binaryValue == '00' + binaryValue
        else:
            binaryValue = '0' + binaryValue
        binary_shift = binaryValue[1:] + binaryValue[0]
        string += chr(int(binary_shift,2))
    print(string)

#decryption
def decrypt(s):
  

print("ASCII Text: ")
a=input()                                     #user enters input for encryption
encrypt(a)
print("Text for Decryption: ")
b=input()                                     #user enters input for decryption
decrypt(b)
