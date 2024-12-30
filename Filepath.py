import os  # Importing the 'os' module to interact with the operating system

path = input('Enter a path: ') # Prompt the user to enter a path (file or directory)

print(path) # Print the entered path for confirmation

if os.path.exists(path): # Check if the entered path exists
    print('The path exists')  # Inform the user that the path exists
    
    if os.path.isfile(path): # Check if the path is a file
        with open(path, 'r', encoding='utf-8-sig') as f: # Open the file in read mode with the specified encoding
            lines = f.readlines() # Read all lines from the file
            print(lines) # Print the contents of the file
    
    elif os.path.isdir(path): # Check if the path is a directory
        print('The path is a directory. Here are its contents:')
        for filename in os.listdir(path): # List all files and directories within the specified directory
            print(filename) # Print the name of each file and directory

else: # Handle the case where the path does not exist
    print('The specified path does not exist')  # Inform the user that the path does not exist
