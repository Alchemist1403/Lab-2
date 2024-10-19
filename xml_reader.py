import xml.dom.minidom as minidom


xml_file = open('books.xml', 'r') # Чтение файла
xml_data = xml_file.read()


dom = minidom.parseString(xml_data) #распарсить файл
dom.normalize() # оптимизирует работу с файлом

elements = dom.getElementsByTagName('book')

books_dict = {} #Пустой словарь 

for node in elements:
    for child in node.childNodes:
        if child.nodeType == 1:         # 1 - элементный узел (содержит подузлы)
            if child.tagName == 'title':
                if child.firstChild.nodeType == 3: # 3 - узел содержит текст
                    title = child.firstChild.data
            if child.tagName == 'price':
                if child.firstChild.nodeType == 3:
                    price = float(child.firstChild.data)

    books_dict[title] = price

    if node.getAttribute('id') == 'bk104':
        print(node.getElementsByTagName('title')[0].firstChild.data)



for key in books_dict.keys():
    print(key,books_dict[key])


print(books_dict)

xml_file.close()