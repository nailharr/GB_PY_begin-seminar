filename = "phones.txt"


def create_new_contact(contact):
    with open(filename, "a", encoding='UTF-8') as ph:
        ph.writelines(f"{contact}\n")


# def auto_number():
#     with open(filename, "r") as f:
#         lines = len(f.readlines())
#     return lines


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
        lst.sort(key=lambda x: int(x.split(';')[0]))
        print(*lst)


def delete_contact():
    with open(filename, "r", encoding="UTF-8") as ph:
        lst = ph.read()
        lst_lines = lst.split('\n')
        del_index = int(input("Введите номер строки для удаления: ")) - 1
        del_line = lst_lines[del_index]
        lst_lines.pop(del_index)
        print(f"Удалена запись: {del_line}")
        with open(filename, "w", encoding="UTF-8") as file:
            file.write("\n".join(lst_lines))


def change_contact(contact):
    pass
