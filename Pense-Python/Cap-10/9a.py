# Mais Rapido
file = open('words.txt')
words = []
for word in file:
    word = word.strip()
    words.append(word)
