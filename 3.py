import os, shutil


def trans_templates(name):
    if 'templates' not in os.listdir():
        os.mkdir('templates')
    for i in os.listdir(name):
        shutil.move(name + '/' + i, 'templates')


trans_templates(input('Название корневой папки '))
