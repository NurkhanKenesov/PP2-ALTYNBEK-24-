import os

print("Test a path exists or not:")
path = r'C:/Users/user/Desktop/linear algebra'
print(os.path.exists(path))

print("\nFile name of the path:")
print(os.path.basename(path))

print("\nDir name of the path:")
print(os.path.dirname(path))

print("Test a path exists or not:")
path = r'C:\\epicGames\\Tunche.exe'
print(os.path.exists(path))

print("\nFile name of the path:")
print(os.path.basename(path))

print("\nDir name of the path:")
print(os.path.dirname(path))