from datetime import datetime
import os
from NoteClass import Note

cur_path = os.path.dirname(__file__)
print(cur_path)

def read_file():
    try:
        array = []
        file = open("notes.csv", "r", encoding='utf-8')
        notes = file.read().strip().split("\n")
        for n in notes:
            split_n = n.split(';')
            note = Note.Note(
                id = split_n[0], title = split_n[1], body = split_n[2], date = split_n[3])
            array.append(note)
    except Exception:
        print('журнал заметок пустой')
    finally:
        return array
    
def write_file(array, mode):
    file = open("notes.csv", mode='w', encoding='utf-8')
    file.seek(0)
    file.close()
    file = open("notes.csv", mode=mode, encoding='utf-8')
    for notes in array:
        file.write(Note.Note.to_string(notes))
        file.write('\n')
    file.close





# def add_note():
#     title = input("Введите заголовок заметки:\n")
#     body = input("Введите описание заметки:\n")
#     note = Note.Note(title=title, body=body)
#     array_notes = read_file()
#     for i in array_notes:
#         if Note.Note.get_id(note) == Note.Note.get_id(i):
#             Note.Note.set_id(note)
#     array_notes.append(note)
#     wF.write_file(array_notes, 'a')
#     print("Заметка добавлена в журнал!")




# def input_Note():
#     id_Note = New_Id()
#     tittle_Note = Tittle_Note()
#     body_Note = Body_Note()
#     time_Note = datetime.now()
#     with open('Note.csv', 'a', encoding='utf-8') as f:
#             f.write(f"{id_Note};{tittle_Note};{body_Note};{time_Note}\n") 
#             print("Заметка добавлена!")

# def print_Note():
#     idNote = input('Введите номер заметки: \n ')
#     print(f"Вывожу данные из заметки №{idNote}: \n")
#     with open('Note.csv', 'r', encoding='utf-8') as f:
#         data_first = f.readlines()
#         for line in data_first:
#             data = line.strip().split(sep=';')
#             print(f"id:{data[0]}: {data[1]}\n{data[2]}\nДата: {data[3]}\n")


# def print_AllNote():
#     print("\n Вывожу список заметок:\n")
#     with open('Note.csv', 'r', encoding='utf-8') as f:
#         data_first = f.readlines()
#         for line in data_first:
#             data = line.strip().split(sep=';')
#             print(f"id:{data[0]}: {data[1]}\n{data[2]}\nДата: {data[3]}\n")


# def Select_Note():
#     idNote = input('Введите номер заметки:\n')
#     check = False
#     with open('Note.csv', 'r', encoding='utf-8') as f:
#         data_first = f.readlines()
#         for line in data_first:
#             data = line.strip().split(sep=';')
#             if data[0]==idNote:
#                 check = True
#                 print(f"\n Вывожу данные из заметки №{idNote}: \n")
#                 print(f"id:{data[0]}: {data[1]}\n{data[2]}\nДата: {data[3]}\n")
# #                Edit_Note()
#     if check != True:
#         print(f"Несуществует такой заметки!\n")

            

# def Edit_Note(id):
#     with open('Note.csv', 'w', encoding='utf-8') as f:
#         data_first = f.readlines()
#         for line in data_first:
#             data = line.strip().split(sep=';')
#             if data[0]==id:
#                 print(f"Заголовок:{data[1]}")
#                 data[1] = Tittle_Note()
#                 print(f"Текст:{data[2]}")
#                 data[2] = Body_Note()
#                 data[3] = datetime.now()
#                 print(data)
#                 f.write(data) 
#                 print(f"Вывожу данные из заметки №{data[0]}: \n")
#                 print(f"id:{data[0]}: {data[1]}\n{data[2]}\nДата: {data[3]}\n")


# def update_note():
#     with open('Note.csv', 'r', encoding='utf-8') as f:
#         data_first = f.readlines()
#         participants = {}
#         print(data_first)
#         for line in data_first:
#             data = line.strip().split(sep=";")
#             id = data[0]
#             text = data[1:]
#             participants[id] = text
#         print(participants)
#         sorted_data = dict(sorted(participants.items(), key=lambda x: x[0], reverse=False))
#         print(sorted_data)
#     with open('Note.csv', 'w', encoding='utf-8') as f:
#         f.write(sorted_data)

#         # for player , score in participants.items():
#         #     if score > K:
#         #     filter_player[player] = score


# # Сортируем участников по убыванию баллов
#         # sorted_data = dict(sorted(filter_player.items(), key=lambda x: x[1], reverse=True))
    

# def Tittle_Note():
#     tittle_Note = input('Введите заголовок: \n ')
#     return tittle_Note

# def Body_Note():
#     body_Note = input('Введите текст заметки: \n ')
#     return body_Note

# def New_Id():
#     with open('Note.csv', 'r', encoding='utf-8') as f:
#             data_first = f.readlines()
#             new_Id = len(data_first)+1
#     return new_Id