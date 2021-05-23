import os


def starter():
    name1 = 'my_project'
    names2 = ['settings', 'mainapp', 'adminaap', 'authapp']

    command = input('Вы хотите использовать стандартный шаблон?(y/n) ')
    if command == 'n':
        print(f'Старое название корневой папки {name1}')
        name1 = input('Новое название корневой папки ')
        for i in range(len(names2)):
            print(f'Старое название папки - {names2[i]}')
            names2[i] = input('Новое название папки ')

    unavailable = os.listdir()
    while name1 in unavailable:
        name1 = input('Введите другое имя ')
    os.mkdir(name1)
    for i in range(len(names2)):
        while names2[i] in os.listdir(name1 + '/'):
            print(name1, 'папка с таким именем уже существует')
            names2[i] = input('Введите другое имя')
        os.mkdir(name1 + '/' + names2[i])


starter()
