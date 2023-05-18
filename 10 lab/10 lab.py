def p1():
    import json
    file = open('cc.json', 'r', encoding='utf-8')
    l = json.load(file)
    #print(l)
    for key in l:
        s = l.get(key)
    #print(s)
    for i in s:
        i['Название:'] = i.pop('name')
        i['Цена:'] = i.pop('price')
        i['Вес:'] = i.pop('weight')
        for key in i:
            if key == 'available':
                if i.get(key) == True:
                    print('Есть в наличии!')
                else:
                    print('Нет в наличии!')
            else:
                print(key, i.get(key))

def p2():
    import json
    dop = {"products":[]}
    name = str(input('Название: '))
    price = int(input('Цена: '))
    available = bool(input('В наличии? (True/False) '))
    weight = int(input('Вес: '))
    dop["products"].append({"name": name, "price": price, "weight": weight, "available": available})

    file = open('cc.json', 'r', encoding='utf-8')
    l = json.load(file)
    l["products"].extend(dop["products"])
    for key in l:
        s = l.get(key)
    for i in s:
        i['Название:'] = i.pop('name')
        i['Цена:'] = i.pop('price')
        i['Вес:'] = i.pop('weight')
        for key in i:
            if key == 'available':
                if i.get(key) == True:
                    print('Есть в наличии!')
                else:
                    print('Нет в наличии!')
            else:
                print(key, i.get(key))

    with open("сс.json", "w") as file:
        json.dump(l, file, indent=4, ensure_ascii=False)

def p3():
    d = {}

    with open("en-ru.txt", "r") as file:
        for line in file:
            eng = line.split("-")[0].strip()
            rus = line.split("-")[1].strip().split(',')
            for i in rus:
                i = i.strip()
                if i in d.keys():
                    d[i] = d[i] + ", " + eng
                else:
                    d[i] = eng

    with open("ru-en.txt", "w") as file:
        for i in sorted(d.keys()):
            file.writelines(f"{i} - {d[i]}\n")

p2()