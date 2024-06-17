import random
message = "TEST"

# Define the DNA encoding and decoding dictionaries
encoding_dict = {'A': 'AT', 'T': 'UI', 'C': 'CG', 'H': 'HT', 'E': 'EA', 'L': 'LG', 'O': 'OT', 'W': 'WT', 'R': 'RT', 'D': 'DT', ' ': 'SP', 'V': 'VA', 'S': 'SZ', 'B': 'BW', 'I': 'IY'}
#encoding_dict = {'A': 'AT', 'T': 'TA', 'C': 'CG', 'G': 'GC'}
decoding_dict = {v: k for k, v in encoding_dict.items()}

# Function to encrypt a message using DNA encoding
def encrypt(message):
    encrypted = ''
    for char in message:
        if char in encoding_dict:
            encrypted += encoding_dict[char]
    return encrypted

# Function to decrypt a DNA-encoded message
def decrypt(encrypted):
    decrypted = ''
    for i in range(0, len(encrypted), 2):
        pair = encrypted[i: i + 2]
        if pair in decoding_dict:
            decrypted += decoding_dict[pair]
    return decrypted

# Example usage
print("Original Message:", message)

# Encryption
encrypted_message = encrypt(message)
print("Encrypted Message:", encrypted_message)

# Decryption
decrypted_message = decrypt(encrypted_message)
print("Decrypted Message:", decrypted_message)