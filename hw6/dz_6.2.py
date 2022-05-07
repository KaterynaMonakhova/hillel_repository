import os
class FILE_PROC:
    def __init__(self, file_proc, mode):
        self.file_proc = file_proc
        self.mode = mode
        if mode == 'c':
            self.mode = 'w'


    def write(self):
        if os.path.exists(file_proc):

        with open(self.file_proc) as f:
            f.write(self.line + '\n')
            for elem in f:
                print(elem)
            f.close()


    def read(self):
        with open(self.file_proc) as f:
            f = open('r')
            f.readlines()
            f.close()

    # def remove(self):
    #     with open(self.file_proc) as f:
    #         f.replace(self.line, '')
    #         f.close()

file_proc = open('test.txt', 'w')
line = 'hello'
files_processing = FILE_PROC(file_proc, line)
