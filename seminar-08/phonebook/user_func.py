from datetime import datetime


def input_number():
    ask = int(input("1 - Создать новый контакт\n"
                    "2 - Показать список контактов\n"
                    "3 - Найти контакт в справочнике\n"
                    "4 - Отсортировать контакты\n"
                    "5 - Изменить контакт\n"
                    "6 - Удалить контакт\n"
                    "… - \n"
                    "0 - Exit program\n"
                    "-------------------\n"
                    "Выберите действие: "))
    return ask


def input_contact():  # TODO: refactoring need
    contact_list = []
    contact_id = contact_list.append(int(input("Порядковый номер: ")))  # TODO: add autoincrement
    lastname = contact_list.append(input("Фамилия: "))
    name = contact_list.append(input("Имя: "))
    surname = contact_list.append(input("Отчество: "))
    phone_number = contact_list.append(input("Номер телефона: "))
    date_of_birth = contact_list.append(datetime.strptime(input("Дата рождения — DD.MM.YYY: "), '%d.%m.%Y'))
    return contact_list


def input_feature():
    request_feature = input("Введите искомое значение: \n")
    return request_feature



