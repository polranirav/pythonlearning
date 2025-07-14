file = open('newfile.txt','w')
if file:
    print("file is opened successfully")
file.write("Here we write a command")
file.write("Hello users of Np Digital")
file.close()


# Write Mode
# file.write("Hello users of JAVATPOINT")

# close() Method :  terminate the program
# fileobject.close()

fileptr = open("test1.txt", "w")
fileptr.write("Python is the modern programming language. It is done any kind of program in shortest way.")
fileptr.close()

with open("test2.txt", "w") as file2:
    file2.write('Hello coders')
    file2.write('Welcome to Np Digital')

fileptr2 = open("test1.txt","r")
#stores all the data of the file into the variable content
print("The filepointer is at byte :",fileptr2.tell())
content = fileptr2.read(30)
# contents = fileptr.readline()
# print(contents)
# prints the type of the data stored in the file
print(type(content))
#prints the content of the file
print(content)
#closes the opened file
fileptr2.seek(10);
print("After reading, the filepointer is at:",fileptr2.tell())
fileptr.close()

fileptrss = open("newfile.txt","r");
#running a for loop
for i in fileptrss:
    print(i)


fileptrsss = open("file2.txt","x")
print(fileptrsss)
if fileptrsss:
    print("File created successfully")