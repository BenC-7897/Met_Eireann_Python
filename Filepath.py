import os  # Importing the 'os' module to interact with the operating system

# Prompt the user to enter a path (file or directory)
path = input('Enter a path: ')

# Print the entered path for confirmation
print(path)

# Check if the entered path exists
if os.path.exists(path):
    print('The path exists')  # Inform the user that the path exists
    
    # Check if the path is a file
    if os.path.isfile(path):
        # Open the file in read mode with the specified encoding
        with open(path, 'r', encoding='utf-8-sig') as f:
            # Read all lines from the file
            lines = f.readlines()
            # Print the contents of the file
            print(lines)
    
    # Check if the path is a directory
    elif os.path.isdir(path):
        print('The path is a directory. Here are its contents:')
        # List all files and directories within the specified directory
        for filename in os.listdir(path):
            # Print the name of each file and directory
            print(filename)

# Handle the case where the path does not exist
else:
    print('The specified path does not exist')  # Inform the user that the path does not exist
