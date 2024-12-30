import os  # Importing the 'os' module to interact with the operating system

filepath = input("Please enter the file path: ") # Prompt the user to input a file path

print(filepath) # Print the entered file path for confirmation

if os.path.exists(filepath): # Check if the entered file path exists
    print('The path exists')  # Inform the user that the path exists
    
    if os.path.isfile(filepath): # Check if the path is a file
        _, ext = os.path.splitext(filepath) # Split the file path to get the file extension
        
        if ext == '.csv': # Check if the file is a .csv file
            with open(filepath, 'r', encoding='utf-8-sig') as f: # Open the file in read mode with the correct encoding
                lines = f.readlines() # Read all the lines in the file
                print(lines) # Print the contents of the file
        else:
            print('The file is not a .csv file') # Inform the user if the file is not a .csv file
    
    elif os.path.isdir(filepath): # Check if the path is a directory
        print('The path is a directory. Here are its .csv files:')
        for filename in os.listdir(filepath): # List all files in the directory and filter for .csv files
            if filename.endswith('.csv'):
                print(filename) # Print the name of each .csv file in the directory
    
    else: # Handle the case where the path is neither a file nor a directory
        print('The specified path does not exist')
else:
    print('Please provide a path.') # Inform the user that the path does not exist
