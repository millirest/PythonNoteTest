import os
from commands import New_Id, input_Note

cur_path = os.path.dirname(__file__)
os.chdir(cur_path)

# if __name__ == '__main__':
#     interface()


ID = New_Id()
print(ID)

input_Note()