phone_book = {
    'Гулноза Мухамедова': '123-456',
    'Ойдина мухамедова': '234-567',
    
}

def add_contact(name, phone_number):
    phone_book[name] = phone_number

def update_contact(name, phone_number):
    if name in phone_book:
        phone_book[name] = phone_number
        print(f"Контакт {name} обновлен.")
    else:
        print(f"Контакт {name} не найден.")

def delete_contact(name):
    if name in phone_book:
        del phone_book[name]
        print(f"Контакт {name} удален.")
    else:
        print(f"Контакт {name} не найден.")

def find_contact(name):
    if name in phone_book:
        print(f"Номер телефона для {name}: {phone_book[name]}")
    else:
        print(f"Контакт {name} не найден.")

def print_phone_book():
    print("Телефонный справочник:")
    for name, phone_number in phone_book.items():
        print(f"{name}: {phone_number}")

while True:
    print("Выберите:")
    print("1 - добавить")
    print("2 - изменить")
    print("3 - удалить")
    print("4 - найти контакт")
    print("5 - распечатать ")
    print("6 - выход")

    choice = input()

    if choice == '1':
        name = input("Введите ФИО контакта: ")
        phone_number = input("Введите номер телефона: ")
        add_contact(name, phone_number)
        print(f"Контакт {name} успешно добавлен.")
    elif choice == '2':
        name = input("Введите ФИО, которого нужно изменить: ")
        phone_number = input("Введите новый номер телефона контакта: ")
        update_contact(name, phone_number)
    elif choice == '3':
        name = input("Введите ФИО, которого нужно удалить: ")
        delete_contact(name)
    elif choice == '4':
        name = input("Введите ФИО контакта, номер которого нужно найти: ")
        find_contact(name)
    elif choice == '5':
        print_phone_book()
    elif choice == '6':
        break
    else:
        print("Некорректный ввод.")