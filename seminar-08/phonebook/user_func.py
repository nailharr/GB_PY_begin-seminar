from datetime import datetime


def select_action():
    ask = int(input("1 - Создать новый контакт\n"
                    "2 - Показать список контактов\n"
                    "3 - Показать сортированный список контактов\n"
                    "4 - Найти контакт в справочнике\n"
                    "5 - Изменить контакт\n"
                    "6 - Удалить контакт\n"
                    "… - \n"
                    "0 - Exit program\n"
                    "-------------------\n"
                    "Выберите действие: "))
    return ask


def input_contact():  # TODO: refactoring need
    contact_list = []
    lastname = contact_list.append(input("Фамилия: "))
    name = contact_list.append(input("Имя: "))
    surname = contact_list.append(input("Отчество: "))
    phone_number = contact_list.append(input("Номер телефона: "))
    date_of_birth = contact_list.append(datetime.strptime(input("Дата рождения — DD.MM.YYY: "), '%d.%m.%Y'))
    return ';'.join(map(str, contact_list))


def search_feature():
    request_feature = input("Введите поисковой запрос: \n")
    return request_feature


def select_contact():
    ask_number = input("Введите номер контакта для совершения выбранного действия: ")
    return ask_number


def select_field():
    ask_field = int(input("Выберите поле для сортировки:\n"
                          "1 - Фамилия\n"
                          "2 - Имя\n"
                          "3 - Отчество\n"
                          "4 - Номер телефона\n"
                          "5 - Дата рождения\n"))
    return ask_field
