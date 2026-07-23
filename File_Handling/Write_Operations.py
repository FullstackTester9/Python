"""
This program demonstrate write operation on file.
It uses write() and writelines() method.

Modes:
w = Write mode. This mode creates a new file if it does not exist.
If file exist then it will delete its old contents and write new content.

a = Append mode. This mode keeps old text in a file and adds new text at the bottom.
Still you need to add new line '\n' manually.

Methods:
write(text) = Writes text to the file. It does not add new line at the ende of your text. 
You need to add '\n' manually. Accept only string.

writelines(iterable): Used to write multiline text to a file. Still you need to add '\n' manually.
As iterables you can pass list, tuple, sets directly.
"""

# Write text with "w" mode.
try:
    relative_filePath = r"File_Handling\Files\For_Write_w_mode.txt"
    file = open(relative_filePath,'w')

    # Writing text to a file.
    write_line = file.write("Hi,\n\nThis text will be written to the file.")
except Exception as e:
    print(e)
finally:
    print("Write operation with 'w' mode completed successfully...")
    file.close()  
#===========================================================================================

# Write text with "a" mode.
try:
    relative_filePath = r"File_Handling\Files\For_Write_a_mode.txt"
    file = open(relative_filePath,'a')

    # Writing text to a file.
    multi_line = ["This is first line\n", 'This is second line\n', "This is third line.\n\n"]
    write_line = file.writelines(multi_line)
except Exception as e:
    print(e)
finally:
    print("Write operation with 'a' mode completed successfully...")
    file.close()  
