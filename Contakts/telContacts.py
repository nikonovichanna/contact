
import json


def load_contacts():
    try:
        with open('contacts.json', 'r', encoding='utf-8') as file:
            contacts = json.load(file)
    except FileNotFoundError: 
        contacts = []
    return contacts

def save_contacts(contacts):
    with open('contacts.json', 'w', encoding='utf-8') as file:
        json.dump(contacts, file, indent=4, ensure_ascii=False)

def display_contacts(contacts):
    if not contacts:
        print("Справочник пуст.")
    else:
        for contact in contacts:
            print(f"Имя: {contact['name']}")
            print(f"Номер телефона: {contact['phone']}")
            print("==============================")

def add_contact(contacts):
    name = input("Введите имя: ")
    phone = input("Введите номер телефона: ")
    contact = {'name': name, 'phone': phone}
    contacts.append(contact)
    save_contacts(contacts)
    print("Контакт успешно добавлен.")

def import_contacts(contacts):
    try:
        file_name = input("Введите имя файла для импорта: ")
        with open(file_name, 'r') as file:
            imported_contacts = json.load(file)
            contacts.extend(imported_contacts)
            save_contacts(contacts)
            print("Контакты успешно импортированы.")
    except FileNotFoundError:
        print("Файл не найден.")

def search_contact(contacts):
    name = input("Введите имя для поиска: ")
    found_contacts = [contact for contact in contacts if contact['name'] == name]
    if found_contacts:
        print("Результаты поиска:")
        for contact in found_contacts:
            print(f"Имя: {contact['name']}")
            print(f"Номер телефона: {contact['phone']}")
            print("==============================")
    else:
        print("Контакт не найден.")

def delete_contact(contacts):
    name = input("Введите имя контакта, который нужно удалить: ")
    contacts = [contact for contact in contacts if contact['name'] != name]
    save_contacts(contacts)
    load_contacts()
    print("Контакт успешно удален.")

def update_contact(contacts):
    name = input("Введите имя контакта, который нужно обновить: ")
    for contact in contacts:
        if contact['name'] == name:
            new_phone = input("Введите новый номер телефона: ")
            contact['phone'] = new_phone
            save_contacts(contacts)
            print("Контакт успешно обновлен.")
            return
    print("Контакт не найден.")

def main():
    contacts = load_contacts()
    while True:
        print("===== Телефонный справочник =====")
        print("1. Просмотреть контакты")
        print("2. Добавить контакт")
        print("3. Импортировать контакты")
        print("4. Поиск контакта")
        print("5. Удалить контакт")
        print("6. Обновить контакт")
        print("0. Выйти")
        
        choice = input("Выберите действие (введите номер): ")
        
        if choice == '1':
            display_contacts(contacts)
        elif choice == '2':
            add_contact(contacts)
        elif choice == '3':
            import_contacts(contacts)
        elif choice == '4':
            search_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            update_contact(contacts)
        elif choice == '0':
            break
        else:
            print("Некорректный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
