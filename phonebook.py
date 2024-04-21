def main():
    with open('phonebook.txt', 'a', encoding='utf-8'):
        pass
    
    var = 0
    while var != '5':
        print(
            "Выберите действие:\n"
            "1. Добавить контакт.\n"
            "2. Найти контакт.\n"
            "3. Показать телефонную книгу.\n"
            "4. Скопировать контакт.\n"
            "5. Выход.\n"
            )
        print()
        var = input("Выберите вариант: ")
        while var not in "12345":
            print("Некорректный ввод.")
        var = input("Выберите вариант: ")
        print()

        match var:
            case '1':
                add_cont()
            case '2':
                find_cont()
            case '3':
                open_book()
            case '4':
                copy_cont()
            case '5':
                print("Конец программы.")
        print()
        

def create_cont():
    surrname = input_surrname()
    name = input_name()
    patr = input_patr()
    phone = input_phone()
    return f'{surrname} {name} {patr}: {phone}\n\n'

def add_cont():
    contact_str = create_cont()
    with open('phonebook.txt', 'a', encoding='utf-8') as file:
        file.write(contact_str)
def input_surrname():
    return input("Введите фамилию: ").title()
def input_name():
    return input("Введите имя: ").title()
def input_patr():
    return input("Введите отчество: ").title()
def input_phone():
    return input("Введите номер телефона: ")

def open_book():
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        contact_str = file.read()
    contacts_list = contact_str.rstrip().split('\n\n')
    for n, contact in enumerate(contacts_list, 1):
        print(n, contact)

def find_cont():
    print(
        "Варианты поиска:\n"
        "1. По фамилии\n"
        "2. По имени\n"
        "3. По отчеству\n"
        "4. По номеру телефона\n"
    )
    var = input("Выберите вариант: ")
    while var not in "1234":
        print("Некорректный ввод.")
        var = input("Выберите вариант: ")
    i_var = int(var) - 1
    search = input("Введите данные для поиска:").title()
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        contact_str = file.read()
    contacts_list = contact_str.rstrip().split('\n\n')

    for str_contact in contacts_list:
        lst_contact = str_contact.replace(":", "").split()
        if search in lst_contact[i_var]:
            print (str_contact)

def copy_cont():
    print("Выберите контакт для копирования:")
    print()

    with open('phonebook.txt', 'r', encoding='utf-8') as file:
         contact_str = file.read()
    contacts_list = contact_str.rstrip().split('\n\n')

    i_number = []
    for number, contact in enumerate(contacts_list, 1):
        i_number.append(number)
        print(number, contact)
    print()
    number_contact = int(input("Введите номер контакта: "))
    print()

    for number, contact in enumerate(contacts_list, 1):
        if number == number_contact:
            print(contact)
            with open('phonebook_copy.txt', 'a', encoding='utf-8') as file:
                file.write(f"{contact} \n\n")
    print()
    print("Контакт скопирован в файл phonebook_copy.txt.")

    




main()