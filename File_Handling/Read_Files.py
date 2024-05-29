'''
    :4 Different Modes in for opening files.
    1)"r" - Read - Opens file for reading, error if file doesnot exist.
    2)"a" - Append - Open a file for appending, creates file if does not exist.
    3)"w" - Write - Open file for writing, creates file if does not exist.
    4)"x" - Create - Creates the specified file, returns if file exists.

    :read() method returns whole text.
    :You can specify how many character you want to return.
    :Eg: read(5)

    :readline() method returns one line

'''
f=open("read.txt")
print(f.readline())
print(f.read())

f1=open("read2.txt")
print(f1.read(5))

f.close()
f1.close()