'''
    Delete a File:
    :To delete a file, you must import OS module, and run its os.remove() function.

    :To delete a folder, use os.rmdir() function.
'''
import os
if os.path.exists("read2.txt"):
    os.remove("read2.txt")
else:
    print("The file does not Exist.")
