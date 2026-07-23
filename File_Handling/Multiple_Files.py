"""
This program demonstrates reading multiple files.
"""

# Read multiple files using context manager
try:
    f1 = r"File_Handling\Files\For_Read.txt"
    f2 = r"File_Handling\Files\For_Write_a_mode.txt"
    with open(f1,'r') as file_1, open(f2, 'r') as file_2:

        # 1. Print all lines from the first file
        print("--- CONTENT OF For_Read.txt ---")
        for line in file_1.readlines():
            print(line.strip())
            
        print("\n" + "="*50 + "\n") # Visual separator between files
        
        # 2. Print all lines from the second file
        print("--- CONTENT OF For_Wite_a_mode.txt ---")
        for line in file_2.readlines():
            print(line.strip())
except Exception as e:
    print(e)