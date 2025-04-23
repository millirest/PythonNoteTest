import commands as com
#from commands import print_AllNote, input_Note, Select_Note
#from commands import printNenuTitle

def interface():
    while True:
        menu_console()
        user_input = input()
        if user_input == '1':
            com.show("all")
        elif user_input == '2':
            com.show("ID")
        elif user_input == '3':
            com.show("date")
        elif user_input == '4':
            com.show("all")
            com.change_note()
        elif user_input == '5':
            com.add_note()
        elif user_input == '6':
            com.show("all")
            com.del_notes()
        else:
            print("Программа Журнал заметок завершена")
            break

def menu_console():
        print("           Главное меню\n" \
        "           ЖУРНАЛ ЗАМЕТОК")
        print("1 - вывод журнала \n" \
        "2 - вывод заметки по id \n" \
        "3 - выбор заметки по дате\n" \
        "4 - редактирование заметки\n"\
        "5 - добавление заметки\n" \
        "6 - удаление заметки\n" \
        "7 - выход")

        print("\n введите пункт из меню ")

