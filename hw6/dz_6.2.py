class FileMode:
    def __init__(self, path, mode):
        self.path = path
        self.mode = mode

    def __enter__(self):
        self.fmode = open(self.path, self.mode)
        return self.fmode

    def __exit__(self, *ext_info):
        self.fmode.close()
        del self.fmode

def file_mode (path, mode):
    with FileMode(path, mode) as fmode:
        if fmode.mode == 'a':
            fmode.write('test\n')
        elif fmode.mode == 'r':
            for elem in fmode:
                print(elem)
        elif fmode.mode == 'w':
            fmode.write('')

file_mode('out.txt', 'w')
file_mode('out.txt', 'a')
file_mode('out.txt', 'a')
file_mode('out.txt', 'r')