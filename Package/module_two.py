from deep_translator import GoogleTranslator
from langdetect import detect, LangDetectException

def TransLate(text, lang):
    if not text:
        return "Помилка: текст не може бути пустим"
    
    try:
        detected_lang = detect(text)
        if detected_lang == lang:
            return text

        translated = GoogleTranslator(source=detected_lang, target=lang).translate(text)
        return translated
    except LangDetectException as e:
        return f"Помилка визначення мови: {repr(e)}"
    except Exception as e:
        return f"Помилка перекладу: {repr(e)}"

def LangDetect(text):
    if not text:
        return "Помилка: текст не може бути пустим"
    if len(text) < 2:
        return "Помилка: текст занадто короткий для визначення мови"
    
    try:
        lang = detect(text)
        return lang
    except LangDetectException as e:
        return f"Помилка визначення мови: {repr(e)}"

def CodeLang(lang):
    lang_dict = GoogleTranslator().get_supported_languages(as_dict=True)
    
    if lang.lower() in lang_dict.values():
        return list(lang_dict.keys())[list(lang_dict.values()).index(lang.lower())]

    if lang.lower() in lang_dict.keys():
        return lang_dict[lang.lower()]

    return "Помилка: мова або код не розпізнано."

def LanguageList(out="screen", text=None):
    try:
        translator = GoogleTranslator()
        
        header = f"{'N':<5} {'Language':<15} {'ISO-639 code':<15}"
        if text:
            header += "Text"
        print(header)
        print("-" * len(header))
        
        results = []
        
        lang_dict = translator.get_supported_languages(as_dict=True)
        for idx, (name, code) in enumerate(lang_dict.items(), 1):
            if text: 
                translated = translator.translate(text, target=code)
            else:
                translated = ""

            row = f"{idx:<5} {name:<15} {code:<15} {translated}" 
            results.append(row)
        

        if out == "screen":
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
