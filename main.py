"""
Make by Romashov Artem and Vyaltseva Daria.
.
.
.
=D
"""

MORSE_CODE_RU = {'а': '.-',
                 'б': '-...',
                 'в': '.--',
                 'г': '--.',
                 'д': '-..',
                 'е': '.',
                 'ж': '...-',
                 'з': '--..',
                 'и': '..',
                 'й': '.---',
                 'к': '-.-',
                 'л': '.-..',
                 'м': '--',
                 'н': '-.',
                 'о': '---',
                 'п': '.--.',
                 'р': '.-.',
                 'с': '...',
                 'т': '-',
                 'у': '..-',
                 'ф': '..-.',
                 'х': '....',
                 'ц': '-.-.',
                 'ч': '---.',
                 'ш': '----',
                 'щ': '--.-',
                 'ъ': '.--.-.',
                 'ы': '-.--',
                 'ь': '-..-',
                 'э': '..-..',
                 'ю': '..--',
                 'я': '.-.-',
                 '@': '.−−.−.',
                 '+': '.-.-.',
                 '!': '--..--',
                 '?': '..--..',
                 ';': '-.-.-.',
                 ':': '---...',
                 ',': '.−.−.−',
                 '.': '......',
                 '1': '.----',
                 '2': '..---',
                 '3': '...--',
                 '4': '....-',
                 '5': '.....',
                 '6': '-....',
                 '7': '--...',
                 '8': '---..',
                 '9': '----.',
                 '0': '-----',
                 "'": '.----.',
                 '"': '.-..-.',
                 '-': '-....-',
                 '_': '..--.-',
                 ' ': ' '}
MORSE_CODE_EN = {'a': '.-',
                 'b': '-...',
                 'c': '-.-.',
                 'd': '-..',
                 'e': '.',
                 'f': '..-.',
                 'g': '--.',
                 'h': '....',
                 'i': '..',
                 'j': '.---',
                 'k': '-.-',
                 'l': '.-..',
                 'm': '--',
                 'n': '-.',
                 'o': '---',
                 'p': '.--.',
                 'q': '--.-',
                 'r': '.-.',
                 's': '...',
                 't': '-',
                 'u': '..-',
                 'v': '...-',
                 'w': '.--',
                 'x': '-..-',
                 'y': '-.--',
                 'z': '--..',
                 '@': '.−−.−.',
                 '+': '.-.-.',
                 '!': '--..--',
                 '?': '..--..',
                 ';': '-.-.-.',
                 ':': '---...',
                 ',': '.−.−.−',
                 '.': '......',
                 '1': '.----',
                 '2': '..---',
                 '3': '...--',
                 '4': '....-',
                 '5': '.....',
                 '6': '-....',
                 '7': '--...',
                 '8': '---..',
                 '9': '----.',
                 '0': '-----',
                 "'": '.----.',
                 '"': '.-..-.',
                 '-': '-....-',
                 '_': '..--.-',
                 ' ': ' '}


def decode_from_morse(code, lang):
    if lang.lower() == "en":
        code = code.split()
        decode = ''
        for elem in code:
            for key, codex in MORSE_CODE_EN.items():
                if elem == codex:
                    decode += key
        return decode.capitalize() if decode.capitalize() != '' \
            else "Something gone wrong. I mean you used letters, buy you should use '.' and '-'"
    elif lang.lower() == "ru":
        code = code.split()
        decode = ''
        for elem in code:
            for key, codex in MORSE_CODE_RU.items():
                if elem == codex:
                    decode += key
        return decode.capitalize() if decode.capitalize() != '' \
            else "Что-то пошло не так. Я думаю вы использовали буквы, а должны были '.' и '-'"


def encode_to_morse(text, lang="en"):
    if lang.lower() == "en":
        text = text.lower()
        encode = []
        for char in text:
            encode.append(MORSE_CODE_EN.get(char))
        return ' '.join(encode)
    elif lang.lower() == "ru":
        text = text.lower()
        encode = []
        for char in text:
            encode.append(MORSE_CODE_RU.get(char))
        return ' '.join(encode)


def main():
    print("Howdy! What's your name?")
    name = input()
    print(f"Hello, {name}! Welcome to our 'Encoder/Decoder Morse code'!"
          f" Please, choose your language (ru/en)")
    while True:
        lang = input()
        if lang.lower() == "ru" or lang.lower() == "en":
            break
        print("Incorrect request!")
        print(f"Hello, {name}! Welcome to our 'Encoder/Decoder Morse code'!"
              f" Please, choose your language (ru/en)")
    if lang.lower() == "ru":
        while True:
            print("ПРЕДУПРЕЖДЕНИЕ!\n"
                  "Наша программа умеет кодировать и декодировать сообщения на двух языках!"
                  "Но она пока не научилась отличать строчные буквы от заглавных, поэтому сообщения"
                  "могут декодироваться с небольшой неточностью.\n"
                  "Также вы в любое время можете ввести '/exit' для выхода из программы.")
            print("Что Вы хотите сделать: закодировать или декодировать сообщение?")

            while True:
                request = input()
                if request.lower() != 'декодировать' and request.lower() != 'закодировать':
                    print("Неправильно введен запрос!")
                    print("Что Вы хотите сделать: закодировать или декодировать сообщение?")
                    continue
                elif request.lower() == "/exit":
                    exit()
                break

            print(f"Введите сообщение, которое Вы хотите {request}:")
            if request.lower() == 'декодировать':
                print(decode_from_morse(input(), "ru"))
            else:
                print(encode_to_morse(input(), "ru"))
            print("Хотите сделать что-то еще?")
            print(f'{name.capitalize()}, вы хотите еще раз протестировать нашу программу?')
            while True:
                request = input()
                if request.lower() == 'нет':
                    exit()
                elif request.lower() == "да":
                    break
                elif request.lower() == "/exit":
                    exit()
                print("Неправильно введен запрос!")
                print(f'{name.capitalize()}, вы хотите еще раз протестировать нашу программу?')
    else:
        while True:
            print("ATTENTION!\n"
                  "Our program can encode or decode to/from Morse code from/to text!"
                  "( but when program decoding text all letters will lowercase =D )\n"
                  "U can type (anytime) '/exit' to exit the program as well.")
            print("What do you want?: encode or decode text?")

            while True:
                request = input()
                if request.lower() != 'decode' and request.lower() != 'encode':
                    print("Incorrect request!")
                    print("What do you want?: encode or decode text?")
                    continue
                elif request.lower() == "/exit":
                    exit()
                break

            print(f"Type text, which you want {request}:")
            if request.lower() == 'decode':
                print(decode_from_morse(input(), "en"))
            else:
                print(encode_to_morse(input(), "en"))
            print(f'{name.capitalize()}, do you want to test our program one more time')
            while True:
                request = input()
                if request.lower() == 'no' or request.lower() == "nope":
                    exit()
                elif request.lower() == "yes" or request.lower() == "yeah" or request.lower() == "yep":
                    break
                print("Incorrect request!")
                print(f'{name.capitalize()}, do you want to test our program one more time')


main()
