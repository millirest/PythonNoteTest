from datetime import datetime
import os

cur_path = os.path.dirname(__file__)
print(cur_path)

def input_Note():
    id_Note = New_Id()
    tittle_Note = Tittle_Note()
    body_Note = Body_Note()
    time_Note = datetime.now()
    with open('Note.csv', 'a', encoding='utf-8') as f:
            f.write(f"{id_Note};{tittle_Note};{body_Note};{time_Note}\n") 
            print("Заметка добавлена!")

def print_Note():
    idNote = input('Введите номер заметки: \n ')
    print(f"Вывожу данные из заметки №{idNote}: \n")
    with open('Note.csv', 'r', encoding='utf-8') as f:
        data_first = f.readlines()
        for line in data_first:
            data = line.strip().split(sep=';')
            print(f"id:{data[0]}: {data[1]}\n{data[2]}\nДата: {data[3]}\n")


def print_AllNote():
    print("\n Вывожу список заметок:\n")
    with open('Note.csv', 'r', encoding='utf-8') as f:
        data_first = f.readlines()
        for line in data_first:
            data = line.strip().split(sep=';')
            print(f"id:{data[0]}: {data[1]}\n{data[2]}\nДата: {data[3]}\n")


def Select_Note():
    idNote = input('Введите номер заметки:\n')
    check = False
    with open('Note.csv', 'r', encoding='utf-8') as f:
        data_first = f.readlines()
        for line in data_first:
            data = line.strip().split(sep=';')
            if data[0]==idNote:
                check = True
                print(f"\n Вывожу данные из заметки №{idNote}: \n")
                print(f"id:{data[0]}: {data[1]}\n{data[2]}\nДата: {data[3]}\n")
#                Edit_Note()
    if check != True:
        print(f"Несуществует такой заметки!\n")

            

def Edit_Note(id):
    with open('Note.csv', 'w', encoding='utf-8') as f:
        data_first = f.readlines()
        for line in data_first:
            data = line.strip().split(sep=';')
            if data[0]==id:
                print(f"Заголовок:{data[1]}")
                data[1] = Tittle_Note()
                print(f"Текст:{data[2]}")
                data[2] = Body_Note()
                data[3] = datetime.now()
                print(data)
                f.write(data) 
                print(f"Вывожу данные из заметки №{data[0]}: \n")
                print(f"id:{data[0]}: {data[1]}\n{data[2]}\nДата: {data[3]}\n")

def Tittle_Note():
    tittle_Note = input('Введите заголовок: \n ')
    return tittle_Note

def Body_Note():
    body_Note = input('Введите текст заметки: \n ')
    return body_Note

def New_Id():
    with open('Note.csv', 'r', encoding='utf-8') as f:
            data_first = f.readlines()
            new_Id = len(data_first)+1
    return new_Id



