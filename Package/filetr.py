import os
from module_one import TransLate  
from module_two import TransLate as DeepTransLate 

os.chdir('D:/Labs/Package') # Зміна робочого каталогу на 'Package'

def read_config(config_file):
    config = {}
    if not os.path.isfile(config_file):
        return f"Помилка: Файл конфігурації '{config_file}' не знайдено."
    try:
        with open(config_file, 'r') as file:
            for line in file:
                if '=' in line:
                    key, value = line.strip().split('=', 1)
                    config[key] = value
        return config
    except Exception as e:
        return f"Помилка читання конфігураційного файлу: {repr(e)}"

def process_file(file_name, target_language, output_mode, max_characters, max_words, max_sentences):
    if not os.path.isfile(file_name):
        return "Файл не знайдено."

    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            text = file.read()
        
        #Перевірка обмежень:
        num_chars = len(text)
        num_words = len(text.split())
        num_sentences = text.count('.') + text.count('!') + text.count('?')
        
        if num_chars > int(max_characters) or num_words > int(max_words) or num_sentences > int(max_sentences):
            return "Текст перевищує задані обмеження."
        
        #Використання функцій перекладу з модулів, які до цього розробив
        translated_text = DeepTransLate(text, target_language)  #Використовуйте DeepTransLate для module_two

        if output_mode == "screen":
            print(f"Переклад на {target_language}:")
            print(translated_text)
        elif output_mode == "file":
            output_file = f"{os.path.splitext(file_name)[0]}_{target_language}.txt"
            with open(output_file, 'w', encoding='utf-8') as file:
                file.write(translated_text)
            return f"Таблиця збережена у файл '{output_file}'"
        else:
            return "Невірний режим виводу."
        
        return "Ok"

    except Exception as e:
        return f"Помилка обробки файлу: {repr(e)}"

config_file = 'D:/Labs/Package/config.txt' #тут початок читання конфігураційного файлу
config = read_config(config_file)
if isinstance(config, dict):
    result = process_file(
        config.get('file_name'),
        config.get('target_language'),
        config.get('output_mode'),
        config.get('max_characters'),
        config.get('max_words'),
        config.get('max_sentences')
    )
    print(result)
else:
    print(config)
