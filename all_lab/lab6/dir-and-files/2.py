import os

print('Exist:', os.access('C:/Users/user/Desktop/linear algebra/1.txt', os.F_OK))
print('Readable:', os.access('C:/Users/user/Desktop/linear algebra/1.txt', os.R_OK))
print('Writable:', os.access('C:/Users/user/Desktop/linear algebra/1.txt', os.W_OK))
print('Executable:', os.access('C:/Users/user/Desktop/linear algebra/1.txt', os.X_OK))