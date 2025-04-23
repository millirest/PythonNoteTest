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
            print("Замтка добавлена!")


def print_Note(id):
    Body_Note = input('Введите номер заметки: \n ')
    print(f"Вывожу данные из заметки №{id}: \n")
    with open('Note.csv', 'r', encoding='utf-8') as f:
        data_first = f.readlines()
        data_first_list = []
        j = 0
        for i in range(len(data_first)):
            if data_first[i] == '\n' or  i == len(data_first)-1:
                data_first_list.append(''.join(data_first[j:i+1]))
                j = i
        print(''.join(data_first_list))

def print_AllNote():
    print("\nВывожу список заметок:\n")
    with open('Note.csv', 'r', encoding='utf-8') as f:
        data_first = f.readlines()
        for line in data_first:
            data = line.strip().split(sep=';')
            print(f"id:{data[0]}: {data[1]}\n{data[2]}\nДата: {data[3]}\n")


def Tittle_Note():
    Tittle_Note = input('Введите заголовок: \n ')
    return Tittle_Note

def Body_Note():
    Body_Note = input('Введите текст заметки: \n ')
    return Body_Note

def New_Id():
    with open('Note.csv', 'r', encoding='utf-8') as f:
            data_first = f.readlines()
            new_Id = len(data_first)+1
    return new_Id



