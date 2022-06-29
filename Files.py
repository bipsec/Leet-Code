import os.path
import logging as lg

# lg.basicConfig(filename='/content/oops.log', level=lg.INFO)


class Data:
    value = "METADATA"

    def __init__(self, fileName, fileType, date, size):
        self.fileName = fileName
        self.fileType = fileType
        self.date = date
        self.size = size

    def fileOpen(self):
        if os.path.isfile(self.fileName):
            with open(f"{self.fileName}.txt", "w") as f:
                f.read(self.fileName)
                print("File Opened Successfully!")
                # lg.info("Creating a file")
                # lg.info("Writing on the file")
                # lg.info(self.fileName)
                f.close()
            return self.fileName
        else:
            try:
                with open(f"{self.fileName}.txt", "w") as f:
                    f.write("This is a new file")
                    print("File Opened when there is no File")
                    # lg.info("Creating a file")
                    # lg.info("Writing on the file")
                    # lg.info(self.fileName)
                    f.close()
                return self.fileName
            except Exception as e:
                print(e)

    def fileRead(self):
        try:
            with open(f"{self.fileName}.txt", "r") as f:
                for i in f:
                    print(i)
        except Exception as e:
            print(e)

    def fileAppend(self):
        try:
            with open(f"{self.fileName}.txt", "a") as f:
                f.write("\nThis is appending in the file")
                print("File Is Appended Successfully!")
                # lg.info("Creating a file")
                # lg.info("Writing on the file")
                # lg.info(self.fileName)
                f.close()
            return self.fileName
        except Exception as e:
            print(e)


# import os.path
# class Data:
#     def __init__(self, filename, filetype, date, size):
#         self.filename = filename
#         self.filetype = filetype
#         self.date = date
#         self.size = size
#
#     def fileopen(self):
#
#         if os.path.isfile(self.filename):
#             with open(f"{self.filename}.txt", "w") as f:
#                 f.read(self.filename)
#                 f.close()
#         else:
#             try:
#                 with open(f"{self.filename}.txt", "w") as f:
#                     f.read(self.filename)
#                     f.close()
#             except Exception as e:
#                 print(e)
#
#     def fileRead(self):
#         try:
#             with open(f"{self.filename}.txt", "w") as f:
#                 f.write("File Created\n A new line is also added")
#                 f.read(self.filename)
#                 f.close()
#         except Exception as e:
#             print(e)
#
#     def fileAppend(self):
#         try:
#             with open(f"{self.filename}.txt", "a") as f:
#                 f.write("\nA new line appended")
#                 f.read(self.filename)
#                 f.close()
#         except Exception as e:
#             print(e)


data = Data("fileB.txt", "2022-01-02", "2MB", "text")
print(data.fileOpen())
print(data.fileRead())
print(data.fileAppend())
print(data.__class__.value)


