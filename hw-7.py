 # Запрашиваем стихотворение 
poem = input("Введите стихотворение: ")

# Разбиваем стихотворение на фразы
phrases = poem.split()

# Создаем список для хранения числа гласных 
vowel_counts = []

# определяем число гласных
for phrase in phrases:
    # Разбиваем фразу на слова
    words = phrase.split("-")
    # Считаем число гласных 
    vowel_count = sum([1 for word in words for letter in word if letter in "aeiouAEIOU"])
    # Добавляем число гласных в список
    vowel_counts.append(vowel_count)

# Проверяем, все ли числа в списке равны
if len(set(vowel_counts)) == 1:
    print("Парам пам-пам")
else:
    print("Пам парам")