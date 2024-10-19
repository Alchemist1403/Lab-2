from csv import reader 
# Найти Книги, названия которых содержат более 30 символов

count = 0
with open('books-en.csv', 'r', encoding='windows-1251') as csvfile:
    file = reader(csvfile, delimiter=';')
    books_data = [i for i in file]
    books_data.pop(0)
    for row in books_data:
        lower_case = row[1].lower()
        if len(lower_case) > 30:
            count += 1

print(f"Книги, название которых содержит более 30 символов: {count}")