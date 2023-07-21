def create_new_contact(contact):
    with open("phones.txt", "a", encoding='UTF-8') as ph:
        ph.writelines(f"{contact}\n")


def find_contact(feature):
    count = 0
    with open("phones.txt", "r", encoding='UTF-8') as ph:
        lst = ph.readlines()
        for row in lst:
            if feature in row:
                count += 1
                print(f"{count} - {row.strip()}")
    return f'\nНайдено контактов: {count}'


def sort_contacts():
    # with open("phones.txt", "r", encoding='UTF-8') as ph:
    #     lst = ph.readlines()
    # with open("phones.txt", "w", encoding='UTF-8') as ph:
    #     lst_s = ph.readlines()
    #     lst_s.sort(key=lambda x: x.split(',')[0])



def delete_contact(contact):
    pass


def change_contact(contact):
    pass
