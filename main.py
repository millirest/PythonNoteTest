import os
from ui import interface
from commands import update_note
print("Добрый день, это спецаилный бот для заметок \n")
cur_path = os.path.dirname(__file__)
os.chdir(cur_path)

# if __name__ == '__main__':
#     interface()

update_note()