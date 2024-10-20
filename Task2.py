import xml.dom.minidom as minidom


xml_file = open('currency.xml', 'r') # Чтение файла
xml_data = xml_file.read()

dom = minidom.parseString(xml_data) #распарсить файл
dom.normalize() # оптимизирует работу с файлом

elements = dom.getElementsByTagName('Valute')

Charcode_nominal_dict = {} #Пустой словарь 

Charcode = ''
Nominal = ''

for node in elements:
    for child in node.childNodes:
        if child.nodeType == 1:         # 1 - элементный узел (содержит подузлы)
            if child.tagName == 'CharCode':
                if child.firstChild.nodeType == 3: # 3 - узел содержит текст
                    Charcode = child.firstChild.data
            if child.tagName == 'Nominal':
                if child.firstChild.nodeType == 3:
                    Nominal = int(child.firstChild.data)

    Charcode_nominal_dict[Charcode] = Nominal

print(Charcode_nominal_dict)

xml_file.close()
            