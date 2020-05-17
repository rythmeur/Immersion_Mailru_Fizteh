class FileReader:
    import os.path

    def __init__(self, path):
        self.path = path

    def read(self):
        try:
            with open(self.path) as f:
                content = f.read()
            return content
        except FileNotFoundError as err:
            #print("ERROR!!!", err.args[0],err.args[1])
            return ""


        # with open(self.path) as f:
        #     content = f.read()
        # return content




def main():
    reader = FileReader(r"D:\Etude\Stanford\2018 Программирование на Pyhon\Погружение в Python\Homework\week3\1\1.txt")
    text = reader.read()
    print("text= ", text)

    reader2 = FileReader(r"C:\1.txt")
    text2 = reader2.read()
    print("text2= ", text2)


if __name__ == "__main__":
    # execute only if run as a script
    main()