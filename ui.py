def interface():
    print("Добрый день, это спецаилный бот для заметок \n" \
    "Что вы хотите сделать?\n" \
    "1 - Показать все заметки\n" \
    "2 - Редактировать заметки" \
    "3 - Запись даных\n")
    command = int(input('Введите число:\n'))

    while command !=1 and command !=2 :
        print("Неправильный ввод")
        command = int(input('Введите число:\n'))

   

    if command == 1:
        input_data()
    elif command == 2:
        print_data() 