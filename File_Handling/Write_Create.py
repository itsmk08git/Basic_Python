'''
    :"w" - Write- This Mode will overwrite any existing content.
    :"a" - Append - This Mode will append to the end of the file.
'''

f=open("write.txt", "w")
f.write("Hello Mr.Mk, Welcome to the text file.")

f1=open("write.txt", "a")
f1.write("\nThis File is very intresting.")

f2=open("read2.txt", "w")
f2.write("What is up people.")