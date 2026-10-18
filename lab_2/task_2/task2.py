from collections import Counter
import json

def load_text(filename):
    try:
        with open(filename, encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Ошибка: файл {filename} не найден")
        raise

def print_stats(text):
    total = len(text)
    chars = Counter(text)
    print(f"Всего: {total}, Уникальных: {len(chars)}\n")
    for c, cnt in sorted(chars.items(), key=lambda x: -x[1]):
        print(f"{c:<16} | {cnt:6} | {cnt / total:.4f}")

def replace_interactive(text):
    reps = {}
    while True:
        print(f"\nТекст:\n{text[:200]}\n")
        old = input("\nСимвол для замены (Enter - выход): ")
        if not old:
            break
        
        if old == " ":
            new = input("Заменить ПРОБЕЛ на: ")
            reps[old] = new
            text = text.replace(old, new)
        elif old == "\n":
            new = input("Заменить ПЕРЕВОД СТРОКИ на: ")
            reps[old] = new
            text = text.replace(old, new)
        else:
            new = input(f"Заменить '{old}' на: ")
            reps[old] = new
            text = text.replace(old, new)
            
    return reps, text

def main():
    text = load_text('original.txt')
    print_stats(text)
    reps, new_text = replace_interactive(text)
    
    with open('decrypted.txt', 'w', encoding='utf-8') as f:
        f.write(new_text)
    with open('key.json', 'w', encoding='utf-8') as f:
        json.dump(reps, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    main()
