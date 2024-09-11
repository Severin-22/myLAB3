from googletrans import Translator, LANGUAGES
import langid

translator = Translator()

def TransLate(text, lang):
    if not text:
        return "Помилка: текст не може бути пустим"

    try:
        detected_lang = translator.detect(text).lang
        if detected_lang == lang:
            return text

        translated = translator.translate(text, dest=lang)
        return translated.text
    except Exception as e:
        return f"Помилка перекладу: {repr(e)}"  

def LangDetect(text):
    if not text:
        return "Помилка: текст не може бути пустим"
    if len(text) < 2:
        return "Помилка: текст короткий для визначення мовви"
        
    try:
        lang, confidence = langid.classify(text)
        return lang, confidence
    except Exception as e:
        return f"Помилка визначення мови: {repr(e)}"
  
def CodeLang(lang):
    if not lang:
        return "Введіть lang"
    
    lowerCase = lang.lower()
    
    # Тут йде перевірка чи lang є кодом мови у словнику бібліотеки
    if lowerCase in LANGUAGES:
        return LANGUAGES[lowerCase]
    
    # Тут у мене йде перевірка чи lang є назвою мови. У name in LANGUAGES.items() йде ітерація у словнику
    code_dictionary = {name.lower(): code for code, name in LANGUAGES.items()}
    if lowerCase in code_dictionary:
        return code_dictionary[lowerCase]
    
    return "Помилка: мова або код не розпізнано."


def LanguageList(out="screen", text=None):
    try:
        translator = Translator()
        
        # Назви стовпців
        header = f"{'N':<5} {'Language':<15} {'ISO-639 code':<15}"
        if text:
            header += "Text"
        print(header)
        print("-" * len(header))
        
        # тут створив список для зберігання результатів
        results = []
        
        # тут я переклав тексту на всі  мови які можна
        for idx, (code, lang) in enumerate(LANGUAGES.items(), 1):
            if text: # на цьому рядку отримую переклад переданий
                translated = translator.translate(text, dest=code).text
            else:
                translated = ""

            row = f"{idx:<5} {lang:<15} {code:<15} {translated}" # тут формується рядок таблиці
            results.append(row)
        
        if out == "screen": # результат виводитьс або на екран або у файл, залежить від аргумента
            for row in results:
                print(row)
        elif out == "file":
            with open("language_list.txt", "w", encoding="utf-8") as f:
                f.write(header + "\n")
                f.write("-" * len(header) + "\n")
                for row in results:
                    f.write(row + "\n")
            print("Таблиця збережена у файл 'language_list.txt'")
        
        return "Ok"
    
    except Exception as e:
        return f"Помилка: {repr(e)}"