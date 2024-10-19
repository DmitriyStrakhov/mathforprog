def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

def caesar_decipher(text, shift):
    return caesar_cipher(text, -shift)

def main():
    while True:
        choice = input("(1) Зашифровать (2) Расшифровать (3) Выйти: ")
        if choice == '1':
            text = input("Введите текст для шифрования: ")
            shift = int(input("Введите значение сдвига: "))
            encrypted_text = caesar_cipher(text, shift)
            print(f"Зашифрованный текст: {encrypted_text}")
        elif choice == '2':
            text = input("Введите текст для расшифровки: ")
            shift = int(input("Введите значение сдвига: "))
            decrypted_text = caesar_decipher(text, shift)
            print(f"Расшифрованный текст: {decrypted_text}")
        elif choice == '3':
            break
        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")

if __name__ == "__main__":
    main()