import random
import re
import pandas as pd



print("Биграмма букв - это пара букв, которые стоят рядом в слове. Например, в слове 'кот' биграммы это '^к', 'ко', 'от', и 'т$'11' (^ и $ — начало и конец слова.)")
functions = input("Что вы хотите?\n1. Генератор имен\n2. Таблица расспростроение биграмм?\n3. Придумать свое имя")
if functions == "1":
    with open('names.txt', 'r') as file:
        text = file.read()
    words = re.findall(r'\b\w+\b', text)
    random_word = random.choice(words)
    print(random_word)
elif functions == "2":
    path1 = "Nfactorialtask.xlsx"
    df1 = pd.read_excel(path1)
    pd.set_option("display.width", None)
    pd.set_option("display.max_rows", None)
    pd.set_option("display.max_columns", None)
    print(df1.to_string())
elif functions == "3":
    numofbi = int(input("Сколько вы хотите биграмм в вашем имени? (от 1 до 6)\n Кстати первая биграмма должна начинаться с '^', а последняя заканчиваться на '$': "))
    if numofbi < 1 or numofbi > 6:
        print("Неправильный ввод!")
    else:
        bigrams = []
        for i in range(numofbi):
            bigram = input(f"Введите биграмму #{i+1}: ")
            bigrams.append(bigram)
            name = "".join(bigrams)
        print("Ваше придуманное имя: " + name)
