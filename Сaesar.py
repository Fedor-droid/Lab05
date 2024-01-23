def encrypt_caesar(plaintext, shift):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            shift_val = 1040 if char.isupper() else 1072
            encrypted_char = chr((ord(char) - shift_val + shift) % 32 + shift_val)
            ciphertext += encrypted_char
        else:
            ciphertext += char
    return ciphertext

def decrypt_caesar(ciphertext, shift):
    return encrypt_caesar(ciphertext, -shift)

def main():
    text = input("Введите текст для шифрования: ")
    shift = int(input("Введите шаг сдвига: "))

    encrypted_text = encrypt_caesar(text, shift)
    print("Зашифрованный текст:", encrypted_text)

    decrypted_text = decrypt_caesar(encrypted_text, shift)
    print("Расшифрованный текст:", decrypted_text)

if __name__ == "__main__":
    main()