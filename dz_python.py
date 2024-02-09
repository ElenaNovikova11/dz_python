# Дополнить справочник возможностью копирования данных 
# из одного файла в другой. Пользователь вводит номер 
# строки, которую необходимо перенести из одного файла 
# в другой.

# Данное решение представлено под цифрой 4

def read_sprav():
    sprav = []
    path = 'tel_sprav.txt'
    tel_sprav = open(path, 'r', encoding='utf-8')
 
    for line in tel_sprav:
        n = line.split()
        
        dict_ = {
            "last_name": n[0],
            "first_name": n[1],
            "second_name": n[2],
            "tel": n[3],
        }
      
        sprav.append(dict_)

    tel_sprav.close()
    return sprav
 
def print_sprav(tel_sprav):
    for item in tel_sprav:
          print(*(f"{v}" for v in item.values()))
      
    return None
 
def add_contact():
    tel_sprav = open('tel_sprav.txt', 'a', encoding='utf-8')
    s = input("Введите ФИО, тел, резделенные пробелами: ")
    # ToDo: использовать str.capitalize()
    tel_sprav.write(f'{s}\n')
    tel_sprav.close()
    # print("Такого нет значения")

 
def find_last_name(last_name: str, my_sprav: list[dict[str, str]]=None):
    for item in my_sprav:
        if item["last_name"] == last_name.capitalize():
            print(item)

def copy_line():
    path = open('tel_sprav.txt')
    new_path = open('new_tel_sprav.txt','w')
    line_number = int(input("Введите номер строки"))
    if (line_number) <= 5:
        sprav=[line_number]        
        for linenum, line in enumerate(path):
            if linenum+1 in sprav:
                new_path.write(line)
    else:
        print('Такой строки нет')
    path.close()
    new_path.close()

def main():
    # переменная = open ('название файла', 'режим работы', encoding='кодировка')
    while True:
        print("Что хотите сделать?")
        print("1: Вывести данные")
        print("2: Записать новый контакт")
        print("3: Найти контакт по фамилии")
        print("4: Скопировать строку в новый файл")
        print("0: Выйти")
 
        x = input()
        tel_sprav = read_sprav()
        if x == "1":
            print_sprav(tel_sprav)
        elif x == "2":
            add_contact()
        elif x == "3":
            find_last_name(input("Введите фамилию: "), my_sprav=tel_sprav)
        elif x == "4":
            copy_line()      
        elif x == "0":
            break
        else:
            print("неверная команда")
 
if __name__ == "__main__":
    main()