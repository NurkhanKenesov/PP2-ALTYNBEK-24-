def file_length(file):
        with open(file) as f: #open file and close it(with)
                for i, _ in enumerate(f):
                        pass  #just pass lines and count, nothing to do in _
        return i + 1          #counting starts from 0, thus i+1
    
print("Lines: ", file_length(r'C:/Users/user/Desktop/linear algebra/1.txt'))