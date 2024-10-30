import xml.dom.minidom as minidom


xml_file = open('currency.xml', 'r') # Чтение файла
xml_data = xml_file.read()

dom = minidom.parseString(xml_data) # Распарсить файл
dom.normalize() # Оптимизирует работу с файлом

elements = dom.getElementsByTagName('Valute')

charcode_nominal_dict = {} # Пустой словарь 

charcode = ''
nominal = ''

for node in elements:
    for child in node.childNodes:
        if child.nodeType == 1:         # 1 - элементный узел (содержит подузлы)
            if child.tagName == 'CharCode':
                if child.firstChild.nodeType == 3: # 3 - узел содержит текст
                    charcode = child.firstChild.data
            if child.tagName == 'Nominal':
                if child.firstChild.nodeType == 3:
                    nominal = int(child.firstChild.data)

    charcode_nominal_dict[charcode] = nominal

print(charcode_nominal_dict)

xml_file.close()
            