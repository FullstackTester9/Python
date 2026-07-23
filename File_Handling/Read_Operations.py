"""
This program demonstrate use of read(n), readline(), readlines() functions
to read the file.

read(n) = reads n character from a file.
readline() = return single line from a file.
readlines() = return all lines from a file. use "strip()" to remove extra new lines.
"""

try:
    relative_filePath = r"File_Handling\Files\For_Read.txt"
    file = open(relative_filePath,'r')

    # Reading specified number of character from a file.

    limited_char = file.read(10)
    print(f"Reading specified number of characters only:\n{limited_char}")
except Exception as e:
    print(e)
finally:
    file.close()  

try:
    relative_filePath = r"File_Handling\Files\For_Read.txt"
    file = open(relative_filePath,'r')

    # Reading one line from a file.

    read_one_line = file.readline()
    print(f"Reading one line only:\n{read_one_line}")

except Exception as e:
    print(e)
finally:
    file.close()  

try:
    relative_filePath = r"File_Handling\Files\For_Read.txt"
    file = open(relative_filePath,'r')

    # Reading all lines from a file.
    print(f"Reading all lines:")

    for read_all_line in file.readlines():
        print(read_all_line.strip())
except Exception as e:
    print(e)
finally:
    file.close()  