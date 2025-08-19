import re
from collections import Counter

text = "Mr. and Mrs. Smith have one son and one daughter. The son's name is John. The daughter's name is Sarah. " \
       "The Smiths live in a house. They have a living room. They watch TV in the living room. The father cooks food in the kitchen. " \
       "They eat in the dining room. The house has two bedrooms. They sleep in the bedrooms. They keep their clothes in the closet. " \
       "There is one bathroom. They brush their teeth in the bathroom.The house has a garden. John and Sarah play in the garden. " \
       "They have a dog. John and Sarah like to play with the dog."

# Разбиваем текст на слова (только буквы/цифры/_)
words = re.findall(r"\w+", text)

# Считаем количество вхождений каждого слова
word_counts = Counter(words)

# Выводим только те слова, что встречаются больше 1 раза
for word, count in word_counts.most_common():
    if count > 1:
        print(f"{word}: {count}")