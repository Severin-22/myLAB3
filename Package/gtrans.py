from module_one import TransLate, LangDetect, CodeLang, LanguageList

print("Переклад тексту:")
text = "Добрий день, це Ільєнко Сергій!"
target_language = "en"
translated_text = TransLate(text, target_language)
print(f"Переклад '{text}' на '{target_language}': {translated_text}\n")

print("Визначення мови:")
text_to_detect = "My ice"
detected_language, confidence = LangDetect(text_to_detect)
print(f"Мова тексту '{text_to_detect}' визначена як {detected_language} (А впевненість отака: {confidence})\n")

print("Перевірка коду мови:")
language_code = "en"
language_name = CodeLang(language_code)
print(f"Назва мови для коду '{language_code}': {language_name}\n")

print("Список мов з перекладом:")
output = LanguageList("screen", "Добрий день")
print(f"Результат: {output}\n")
