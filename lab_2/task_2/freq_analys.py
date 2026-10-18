import json
import sys

def load_key(key_file):
    try:
        with open(key_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Ошибка: Файл {key_file} не найден")
        sys.exit(1)

def decrypt_text(encrypted_text, key):
    decrypted = []

    res_str = ""
    for char in encrypted_text:
        if char in key:
            res_str = res_str+key[char]
        else:
            res_str = res_str + char
    return res_str

def main():
    key_file = "key.json"
    input_file = "original.txt"
    output_file = "decrypted.txt"

    key = load_key(key_file)
    
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            encrypted_text = f.read()
    except FileNotFoundError:
        print(f"Ошибка: Файл {input_file} не найден")
        sys.exit(1)

    decrypted_text = decrypt_text(encrypted_text, key)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(decrypted_text)

if __name__ == "__main__":
    main()
