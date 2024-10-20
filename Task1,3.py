from csv import reader 
from random import randint

# Генератор библиографических ссылок

output = open('Book_result.txt', 'w')

with open('books-en.csv', 'r', encoding='windows-1251') as csvfile:
        file = reader(csvfile, delimiter=";")
        books_data = [i for i in file]
        books_data.pop(0)
        for row in range(1,21):
            random_book = books_data[randint(1,len(books_data)-20)]
            print(f'{row}. {random_book[2]}. {random_book[1]} - {random_book[3]}')
            output.write(f'{row}. {random_book[2]}. {random_book[1]} - {random_book[3]}\n')

output.close()
