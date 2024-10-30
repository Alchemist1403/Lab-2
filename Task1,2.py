from csv import reader 


RED = '\u001b[41m' 
LIGHT_GREEN = '\u001b[42m'
YELLOW = '\u001b[43m'
END = '\u001b[0m'


# Поиск по автору

while True:
    count = 0
    request = input("Enter a request: ")
    if request.lower() == 'stop':
        print("Thank you for using!")
        break
    else:
        with open('books-en.csv', 'r', encoding='windows-1251') as csvfile:
            file = reader(csvfile, delimiter=';')
            for row in file:
                lower_case = row[2].lower()
                index = lower_case.find(request.lower())
                if index != -1:
                    if 1997 <= int(row[3]) <= 2000:
                        count +=1
                        print(f"{row[1]} (Author: {row[2]})")

                    # Если ограничение именно на выдачу книги, а не на выдачу результата поиска, используется алгоритм ниже

                    # count +=1
                    # if 1997 <= int(row[3]) <= 2000:
                    #     print(f"{row[1]} (Author: {row[2]})\n  Status: {LIGHT_GREEN}Access is allowed{END}")
                    # else:
                    #     print(f"{row[1]} (Author: {row[2]})\n  Status: {RED}Access denied{END}: You can download only books dated to 1997-2000")
        
        if count == 0:
            print('Nothing found.')
                

