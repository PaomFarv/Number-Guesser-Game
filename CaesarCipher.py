#Caesar Cipher Text Encryption & Decryption (Julius Caesar)
def caesar_cipher_encrypt(text,shift):
    result = ""
    shift_value = shift % 26

    for char in text:
        if char.isalpha():

            if char.islower():
                new_char = chr((ord(char) - ord('a') + shift_value) % 26 + ord('a'))

            elif char.isupper():
                new_char = chr((ord(char) - ord('A') + shift_value) % 26 + ord('A'))

            result += new_char
        
        else:
            result += char

    return result

def caesar_cipher_decrypt(text,shift):
    return caesar_cipher_encrypt(text,-shift)

print("Welcome to the Caesar Cipher text encrypter and decrypter programme.\nDeveloped by PaomFarv.\n\nType (E) to Encrypt text.\nType (D) to Decrypt text.\nType (Q) to quit.")

while True:
    user_response = input("\nYour response (E,D,Q): ").strip().upper()
    
    if user_response == "E":
        text = input("Enter the text to encrypt: ")
        shift = int(input("Enter the shift value: "))

        encrypted_text = caesar_cipher_encrypt(text,shift)
        print("Encrypted Text:",encrypted_text)

    elif user_response == "D":
        text = input("Enter the text to encrypt: ")
        shift = int(input("Enter the shift value: "))
        
        decrypted_text = caesar_cipher_decrypt(text,shift)
        print("Decrypted Text:",decrypted_text)

    elif user_response == "Q":
        print("You are out of the programme.")
        break
    
    else:
        print("Ïnvalid Input.Please Try Again.")