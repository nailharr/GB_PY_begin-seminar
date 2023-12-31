from user_func import select_field
from user_func import select_contact, input_contact

filename = "phones.txt"


def create_new_contact(contact):
    with open(filename, "a", encoding='UTF-8') as ph:
        ph.writelines(f"{contact}\n")


def find_contact(feature):
    with open(filename, "r", encoding='UTF-8') as ph:
        lst = ph.readlines()
        line_count = len(ph.readlines())
        for row in lst:
            if feature in row:
                line_count += 1
                print(f"{lst.index(row) + 1} - {row.strip().split(';')}")
    return print(f'\nНайдено контактов: {line_count}')


def sort_contacts():
    with open(filename, "r", encoding='UTF-8') as ph:
        lst = ph.readlines()
        sort_selector = select_field() - 1
        lst.sort(key=lambda x: x.split(';')[sort_selector])
        print(''.join(lst))


def delete_contact():
    with open(filename, "r", encoding="UTF-8") as ph:
        lst = ph.read()
        lst_lines = lst.split('\n')
        del_index = int(select_contact()) - 1
        del_line = lst_lines[del_index]
        lst_lines.pop(del_index)
        print(f"Удалена запись: {del_line}")
    with open(filename, "w", encoding="UTF-8") as file:
        file.write("\n".join(lst_lines))


def change_contact():
    with open(filename, "r", encoding="UTF-8") as ph:
        lst_f = ph.read()
        lst = lst_f.split('\n')
        edit_index = int(select_contact()) - 1
        edit_line = input_contact()
        print(f"Строка: {lst[edit_index]}\nзаменена на: {edit_line}")
        if edit_index < len(lst):
            lst[edit_index] = edit_line
    with open(filename, "w", encoding="UTF-8") as file:
        file.write('\n'.join(lst))
