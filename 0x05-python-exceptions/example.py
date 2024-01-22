#!/usr/bin/python3
try:
    myfile = open("mydata2.txt")
except FileNotFoundError as ex:
    print("No file found!")
    print(ex.args)

else:
    line_no = 1
    line = myfile.read()
    while (line):
        print("Line no:{} {}" .format(line_no, line))
        line = myfile.read()
        line_no += 1
    myfile.close()
finally:
    file_2 = open("mydata3.txt")
