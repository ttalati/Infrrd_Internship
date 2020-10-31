import random
import os.path


class FileMaker:
    bigfilename = "textBank.txt"
    save_path = "C:/Users/Tejas/PycharmProjects/Tokenizer/data"

    def makefiles(bigfilename="textBank.txt", number=100):
        bigstring = ''
        with open("textBank.txt", 'r') as file:
            bigstring = file.read()

        lastindex = len(bigstring)
        count = 100

        while (count > 0):
            randomnum = random.randint(800, lastindex)
            newString = bigstring[randomnum - 800: randomnum]

            name = os.path.join("C:/Users/Tejas/PycharmProjects/Tokenizer/data", 'testfile' + str(count) + '.txt')
            out = open(name, 'w+')
            newString = newString[newString.find(" ") + 1: len(newString)]
            newString = newString[0: newString.rfind(" ")]
            out.write(newString)
            out.close()
            count = count - 1


FileMaker.makefiles("textBank.txt", 100)
