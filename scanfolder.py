import os, sys
from wand.image import Image

path = os.chdir(r"c:\users\lenovo\documents\iv\Библиотека\scanned_png")

def create_folders(path):
    with open("filenames.txt", "rU") as x:
        for line in x:
            line = line.strip()
            if not os.path.exists(str(line)):
                os.mkdir(str(line))
    return

#create_folders(path)


file_directory = os.chdir(r"c:\users\lenovo\documents\iv\Библиотека\Отсканированная библиотека\2015_02_16")
books = os.listdir(file_directory)
print (books)


for file in books:
    filename = (str(file))
    if filename[-4:] == '.pdf':
        print (str(filename), 'will work')
        with(Image(filename=filename, resolution=120)) as source:
            print (str(os.chdir(os.path.join(r"c:\users\lenovo\documents\iv\Библиотека\scanned_png", filename[:-4]))))
            for i, image in enumerate(source.sequence):
                newfilename = filename[:-4] + str(i + 1) + '.jpeg'
                Image(image).save(filename=newfilename)
    os.chdir(r"c:\users\lenovo\documents\iv\Библиотека\Отсканированная библиотека\2015_02_16")
