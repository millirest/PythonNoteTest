import os
from commands import New_Id, input_Note, print_AllNote

cur_path = os.path.dirname(__file__)
os.chdir(cur_path)

# if __name__ == '__main__':
#     interface()


print_AllNote()