# the with statement and context managers
# mainly used for system resources like
    # files
    # locks
    # network connections and other

# with out "with" we need to open and close the file explicitly
# f = open('hello.txt', 'w')
# try:
#     f.write('hello, world')
# finally:
#     f.close()

# using with statement
# with open('hello.text', 'w') as f:
#     f.write('hellw world')


# context Managers in class based
class ManagedFile:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        self.file = open(self.name, 'w')
        return self.file
    
    def __exit__(self, exc_type, exc_val, exe_tb):
        if self.file:
            self.file.close()

# with ManagedFile('hello.txt') as f:
#     f.write('hello, world')
#     # print(dir(f))

# how it works behind the scene
mf = ManagedFile('hello.txt')
with mf as file:
    file.write('hello world')