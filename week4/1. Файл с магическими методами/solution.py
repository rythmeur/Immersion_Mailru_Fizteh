import os.path
import tempfile

class File:
    def __init__(self, path_to_file):
        self.path_to_file = path_to_file
        if not os.path.exists(path_to_file):
            with open(self.path_to_file, "a") as f:
                f.write('')
        file_in_next = open(self.path_to_file, "r")
        self.file_in_next = file_in_next


    def read(self):
        with open(self.path_to_file, "r") as f:
            content = f.read()


        return content

    def write(self, new_content):
        with open(self.path_to_file, "w") as f:
            f.write(new_content)

    def __str__(self):
        # return f"{self.path_to_file}"
        abs_path_to_file = os.path.abspath(self.path_to_file)
        return "{}".format(abs_path_to_file)

    def __iter__(self):
        return self

    def __next__(self):

        line = self.file_in_next.readline()
        if not line:
            #self.file_in_next.close()
            raise StopIteration
        return line







    @classmethod
    def create_new_file_from_two(cls, path):
        """создает экземпляр класса из словаря с параметрами"""
        return cls(path)

    def __add__(self, obj):
        content_1 = self.read()
        content_2 = obj.read()
        new_content_from_add = content_1 + content_2
        print("len(new_content_from_add) ", len(new_content_from_add))
        print("new_content_from_add\n", new_content_from_add)

        new_temp_path = os.path.join(tempfile.gettempdir(),"new_file" )
        print("new_temp_path ", new_temp_path)
        new_class = self.create_new_file_from_two(new_temp_path)
        print("new_class ", new_class)
        new_class.write(new_content_from_add)

        return new_class


if __name__ == "__main__":
    # execute only if run as a script

    path_to_file = 'some_filename'
    print("os.path.exists(path_to_file)", os.path.exists(path_to_file))
    file_obj = File(path_to_file)
    print("os.path.exists(path_to_file)", os.path.exists(path_to_file))
    print("file_obj.read() ", file_obj.read())
    print("file_obj.write('some text') ", file_obj.write('some text'))
    print("file_obj.read() ", file_obj.read())
    print("file_obj.write('other text')" , file_obj.write('other text'))
    print("file_obj.read() ", file_obj.read())
    print("file_obj ", file_obj)


    file_obj_1 = File(path_to_file + '_1')
    print("type(file_obj_1) ", type(file_obj_1))
    file_obj_2 = File(path_to_file + '_2')
    file_obj_1.write('line 1\n')
    file_obj_2.write('line 2\n')
    new_file_obj = file_obj_1 + file_obj_2
    print("isinstance(new_file_obj, File) ", isinstance(new_file_obj, File))
    print(new_file_obj)
    for line in new_file_obj:
        print(ascii(line))

    r = type(new_file_obj)(path_to_file + '_3')
    print("type(File)(path_to_file + '_3') ", r)