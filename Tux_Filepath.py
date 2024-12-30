import os  # Importing the 'os' module to interact with the operating system

filepath = input("Please enter the file path: ") # Prompt the user to input a file or directory path

print(filepath) # Print the entered file path for confirmation

if os.path.exists(filepath): # Check if the specified path exists
    print('The path exists')  # Inform the user that the path exists
    
    if os.path.isfile(filepath): # Check if the path is a file
        _, ext = os.path.splitext(filepath) # Split the file path to get the file extension

        if ext == '.tux': # Check if the file extension is '.tux'
            with open(filepath, 'r', encoding='utf-8-sig') as f: # Open the .tux file in read mode with the specified encoding
                lines = f.readlines() # Read all lines in the file
                print(lines) # Print the contents of the .tux file
        else:
            print('The file is not a .tux file') # Inform the user if the file is not a .tux file
    
    elif os.path.isdir(filepath): # Check if the path is a directory
        print('The path is a directory. Here are its .tux files:')
        for filename in os.listdir(filepath): # Loop through each file in the directory
            if filename.endswith('.tux'): # Check if the file has a .tux extension
                print(filename) # Print the name of the .tux file
    
    else: # Handle the case where the path is neither a file nor a directory
        print('The specified path does not exist')
else:
    print('Please provide a path.') # Inform the user if the path does not exist

