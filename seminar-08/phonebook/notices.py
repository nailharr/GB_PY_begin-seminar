line = '--------------------------------------\n'


def msg(choice):
    invalid_choice = 'Invalid number of choice. Try again.'
    done_new_contact = 'Контакт успешно добавлен'
    done_change_contact = 'Контакт успешно изменен'
    done_delete_contact = 'Контакт удален'
    end_list = 'Конец списка'
    end_prog = 'Программа завершена'
    end_find = 'Поиск завершен'
    sort_done = 'Контакты отсортированы'

    if choice == 0:
        return end_prog
    elif choice == 1:
        return done_new_contact
    elif choice == 2:
        return end_list
    elif choice == 3:
        return sort_done
    elif choice == 4:
        return end_find
    elif choice == 5:
        return done_change_contact
    elif choice == 6:
        return done_delete_contact
    else:
        return invalid_choice
