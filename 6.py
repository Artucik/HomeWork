# функция для записи числа продаж
# скрипт работает из командной строки
def menu(command):
    def add_new(sale):
        """Функция добавляет кол-во продаж в список продаж"""
        with open('bakery.txt', 'a') as f:
            f.write(str(sale) + '\n')

    def show_sales(flag=''):
        """
        Функция выводит продажи:
        - если не ввести '' в качестве аргумента - вывод всех продаж
        - если ввести above N(номер продажи) - вывод всех продаж над продажей под введенным номером
        - если ввести under N(номер продажи) - вывод всех продаж под продажей под введеным номером
        """
        with open('bakery.txt', 'r') as f:
            # добавление
            if flag == '':
                for numb,i in enumerate(f):
                    print(numb+1, i, end='')

            elif 'under' in flag:
                flag = flag.split()
                sells = f.readlines()
                sells1 = [i.replace('\n', '') for i in sells]

                print(sells1[int(flag[1])-1:])
            elif 'above' in flag:
                flag = flag.split()
                sells = f.readlines()
                sells1 = [i.replace('\n', '') for i in sells]
                print(sells1[:int(flag[1]) - 1 + 1])

    if command == 'add':
        add_new(int(input('Введите кол-во продаж')))
    elif command == 'show':
        show_sales(input('Введите команду(1.ничего | 2.above N | 3.under N) '))
    elif command == 'exit':
        return False


while True:
    if menu(input('Введите команду (1.add 2.show 3.exit) ')) == False:
        break
