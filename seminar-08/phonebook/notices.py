line = '--------------------------------------\n'


def msg(x):
    invalid_choice = 'Invalid number of choice. Try again.'
    done_new_contact = 'Контакт успешно добавлен'
    done_change_contact = 'Контакт успешно изменен'
    done_delete_contact = 'Контакт удален'
    end_list = 'Конец списка'
    end_prog = 'Программа завершена'
    end_find = 'Поиск завершен'
    sort_done = 'Контакты отсортированы'

    if x == 0:
        return end_prog
    elif x == 1:
        return done_new_contact
    elif x == 2:
        return end_list
    elif x == 3:
        return sort_done
    elif x == 4:
        return end_find
    elif x == 5:
        return done_change_contact
    elif x == 6:
        return done_delete_contact
    else:
        return invalid_choice
