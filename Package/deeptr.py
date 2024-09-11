from module_two import TransLate, LangDetect, CodeLang, LanguageList

print("Переклад тексту:")
text_to_translate = "Добрий день, це демонстрація другого модуля!"
target_language = "fr"
translated_text = TransLate(text_to_translate, target_language)
print(f"Переклад '{text_to_translate}' на '{target_language}': {translated_text}\n")

print("Визначення мови:")
text_to_detect = "My ice"
detected_language = LangDetect(text_to_detect)
print(f"Мова тексту '{text_to_detect}' визначена як: {detected_language}\n")

print("Перевірка коду мови:")
language_code_or_name = "fr"
result = CodeLang(language_code_or_name)
print(f"Код/назва для '{language_code_or_name}': {result}\n")

print("Список мов з перекладом:")
output = LanguageList("screen", "Добрий день")
print(f"Результат: {output}\n")
