from csv import reader 
# Найти Книги, названия которых содержат более 30 символов

count = 0
with open('books-en.csv', 'r', encoding='windows-1251') as csvfile:
    file = reader(csvfile, delimiter=';')
    for row in file:
        if len(row[1]) > 30:
            count += 1

print(f"Книги, название которых содержит более 30 символов: {count}")