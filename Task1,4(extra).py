from csv import reader 


# Перечень всех издательств без повторений

publishers = []
with open('books-en.csv', 'r', encoding='windows-1251') as csvfile:
    file = reader(csvfile, delimiter=';')
    books_data = [i for i in file]
    books_data.pop(0)
    for row in books_data:
        publishers.append(row[4])
        
for publisher in set(publishers):
    print(publisher)