import json
import os
import sys
from config import SIZE

def read_key_txt(filename):
    if not os.path.exists(filename):
        raise FileNotFoundError(f"Ошибка: файл {filename} не найден!")
    
    f = open(filename, 'r', encoding='utf-8')
    lines = f.readlines()
    
    square = []
    for line in lines[1:]:
        line = line.rstrip('\n')
        if line:
            chars = line[4:].split('   ')
            square.append(chars)
            
    encrypt_map = {}
    alphabet = ""
    for i in range(SIZE):
        for j in range(SIZE):
            char = square[i][j]
            if char != '*':
                if char == '_':
                    encrypt_map[' '] = f"{i+1:01d}{j+1:01d}"
                    alphabet += ' '
                else:
                    encrypt_map[char] = f"{i+1:01d}{j+1:01d}"
                    alphabet += char
    return encrypt_map, alphabet

def encrypt_polybius(text, encrypt_map):
    res = ""
    for i in range(len(text)):
        try:
            res += encrypt_map[text[i]] + " "
        except:
            res += "?? "
    return res

def main():
    try:
        encrypt_map, _ = read_key_txt('key.txt')
        orig = open('original.txt', 'r').read()
        enc = encrypt_polybius(orig.upper(), encrypt_map)
        out = open('encrypted.txt', 'w')
        out.write(enc)
        print("Done")
    except:
        pass

if __name__ == "__main__":
    main()
