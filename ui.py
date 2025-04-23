from commands import print_AllNote, input_Note, Select_Note

def interface():
    print("Что вы хотите сделать?\n" \
    "1 - Показать все заметки\n" \
    "2 - Добавить заметку\n" \
    "3 - Выбрать заметку\n")
    command = int(input('Введите число:\n'))

    while command !=1 and command !=2 and command !=3:
        print("Неправильный ввод")
        command = int(input('Введите число:\n'))

    if command == 1:
        print_AllNote()
        interface()
    elif command == 2:
        input_Note()
        interface()
    elif command == 3:
        Select_Note()
        interface()
        

def interfaceEdit():
    print("Что с ней сделать?"\
                "1 - Редактировать\n" \
                "2 - Удалить\n" \
                "3 - Выход\n")
    editCommand = int(input('Введите число:\n'))
    while editCommand !=1 and editCommand !=2 and editCommand!=3:
        print("Неправильный ввод")
        editCommand = int(input('Введите число:\n'))
        
    if editCommand == 1:
        pass
    elif editCommand == 2:
        pass
    elif editCommand == 3:
        pass