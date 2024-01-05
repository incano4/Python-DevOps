# написать списковое включение для получения списка букв 
# слова smogtether в верхнем регистре



text = "smogtether"
list = []

# аналог for letter in text: list.append(letter)        - оказалось, питон и так знает, что такое letter...
list = [letter.swapcase() for letter in text] 
print(list)