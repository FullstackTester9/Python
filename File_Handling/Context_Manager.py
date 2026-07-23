"""
This program demonstrate use of context manager. In context manager you dont need to close file.
"""

# Read using context manager
try:
    relative_filePath = r"File_Handling\Files\For_Read.txt"
    with open(relative_filePath,'r') as file:
        for lines in file.readlines():
            print(lines.strip())
except Exception as e:
    print(e)

# Write using context manager
multi_line = ["Grapes", 'Strawberry', "Mango", "Guava", "Avacado"]

try:
    relative_filePath = r"File_Handling\Files\For_Write_a_mode.txt"
    with open(relative_filePath,'a') as file:
        file.writelines(f"{line}\n" for line in multi_line)
except Exception as e:
    print(e)