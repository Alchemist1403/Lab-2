from csv import reader 


top_books_downloads = [0]*20
top_books_name = [0]*20
top20_books = [0]*20

with open('books-en.csv', 'r', encoding='windows-1251') as csvfile:

    file = reader(csvfile, delimiter=';')
    books_data = [i for i in file]
    books_data.pop(0)

    for row in range(20):
        for book in books_data:
            
            if int(book[5]) > top_books_downloads[row] and book[1] not in top_books_name:
                top_books_downloads[row] = int(book[5])
                top_books_name[row] = book[1]

        top20_books[row] = f"{top_books_name[row]} - {top_books_downloads[row]} downloads"

count = 0
for book in top20_books:
    count += 1
    print(f"{count}. {book}")