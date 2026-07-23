"""
This program demonstrate reading of a text file.
I've used absolute path in this program.

NOTE: File "For_Read.txt" should be used for reading purpose only.

Absolute path: Starts from root of the file system.
Relative path: Specifies a location of current working directory (CWD). 
"""

# Uses absolute path
try:
    absolute_filePath = r"D:\MyThings\100DaysOfQA\Study\Python\File_Handling\Files\For_Read.txt"
    file = open(absolute_filePath,'r')
    fileContent = file.read()
    print("Reached location of a file using absolute path:")
    print(f"File contents are:\n{fileContent}", end='\n\n')
except Exception as e:
    print(e)
finally:
    file.close()  

# Uses relative path
try:
    relative_filePath = r"File_Handling\Files\For_Read.txt"
    file = open(relative_filePath,'r')
    fileContent = file.read()
    print("Reached location of a file using relative path:")
    print(f"File contents are:\n{fileContent}")
except Exception as e:
    print(e)
finally:
    file.close()  