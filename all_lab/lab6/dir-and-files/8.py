import os

file = 'test12.py'

if not os.path.exists(file):
    print("No such file")

location = r'C:/Users/user/Desktop/pp2 altynbek 24/all_lab/lab6'

path = os.path.join(location, file)

os.remove(path)