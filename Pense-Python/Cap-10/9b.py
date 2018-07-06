# Mais lento
file = open('words.txt')
words = []
for word in file:
    word = word.strip()
    words = words + [word]
