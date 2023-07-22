from database import *
from user_func import *
from notices import *


def main():
    while True:
        num = select_action()
        if num == 0:
            print(msg(num), line)
            break

        elif num == 1:
            contact = input_contact()
            create_new_contact(contact)
            print(msg(num), line)

        elif num == 2:
            with open("phones.txt", "r") as ph:
                print(ph.read())
                print(msg(num), line)

        elif num == 3:
            sort_contacts()
            print(msg(num), line)

        elif num == 4:
            attribute = search_feature()
            find_contact(attribute)
            print(msg(num), line)

        elif num == 5:
            pass
            print(msg(num), line)

        elif num == 6:
            feature = search_feature()
            find_contact(feature)
            delete_contact()
            print(msg(num), line)

        else:
            print(f"{line}\n{msg(num)}\n\n{line}")


main()
