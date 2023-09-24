d = {
    'а': 'a', 'к': 'k', 'х': 'h', 'б': 'b', 'л': 'l', 'ц': 'c', 'в': 'v', 'м': 'm', 'ч': 'ch',
    'г': 'g', 'н': 'n', 'ш': 'sh', 'д': 'd', 'о': 'o', 'щ': 'shh', 'е': 'e', 'п': 'p', 'ъ': '*',
    'ё': 'jo', 'р': 'r', 'ы': 'y', 'ж': 'zh', 'с': 's', 'ь': "'", 'з': 'z', 'т': 't', 'э': 'je',
    'и': 'i', 'у': 'u', 'ю': 'ju', 'й': 'j', 'ф': 'f', 'я': 'ya'
}


def replace_symbol(c):
    is_upper = False

    if str(c).lower() in d:
        if str(c).isupper():
            is_upper = True
            c = str(c).lower()
        c = d[c]
        if is_upper:
            c = str(c).capitalize()
    return c


def edit_text(text):
    return ''.join(map(replace_symbol, text))


def run():
    with open('cyrillic.txt', encoding='utf-8') as file_in:
        text = file_in.read()

    with open('transliteration.txt', 'w', encoding='utf-8') as file_out:
        file_out.write(edit_text(text))


run()
