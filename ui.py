from commands import print_Note, print_AllNote, input_Note

def interface():
    print("Добрый день, это спецаилный бот для заметок \n" \
    "Что вы хотите сделать?\n" \
    "1 - Показать все заметки\n" \
    "2 - Добавить заметку" \
    "3 - Редактировать заметку\n")
    command = int(input('Введите число:\n'))

    while command !=1 and command !=2 :
        print("Неправильный ввод")
        command = int(input('Введите число:\n'))

   

    if command == 1:
        print_AllNote()
    elif command == 2:
        input_Note()
    elif command == 3:
        

