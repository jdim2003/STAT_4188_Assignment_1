encrypted_file = open("encrypted_message_two.txt", 'r')

encrypted_message = encrypted_file.readline()

encrypted_file.close()

# Write Code Here
def decrypt_transposition_cipher(text):
    chars = list(text)
    length = len(chars)
    for i in range(1, length // 2, 2):
        opposite_index = length - i - 1
        chars[i], chars[opposite_index] = chars[opposite_index], chars[i]
    return ''.join(chars)

with open('encrypted_message_two.txt', 'r') as file:
    encrypted_message = file.read().strip()

decrypted_message = decrypt_transposition_cipher(encrypted_message)
print("Decrypted Message:", decrypted_message)

