# -*- coding: utf-8 -*-
"""
Created on Mon May 27 15:39:19 2024
@author: Bzikangcrane
"""
import os  # Importing the 'os' module to interact with the operating system

# Prompt the user to input a file path
filepath = input("Please enter the file path: ")

# Print the entered file path for confirmation
print(filepath)

# Check if the specified file path exists
if os.path.exists(filepath):
    print('The path exists')  # Inform the user that the path exists

    # Check if the path is a file
    if os.path.isfile(filepath):
        # Split the file path to get the file extension
        _, ext = os.path.splitext(filepath)

        # Check if the file extension is '.cmp'
        if ext == '.cmp':
            # Open the .cmp file in read mode with the specified encoding
            with open(filepath, 'r', encoding='utf-8-sig') as f:
                # Read all lines in the file
                lines = f.readlines()
                # Print the contents of the .cmp file
                print(lines)
        else:
            # Inform the user if the file is not a .cmp file
            print('The file is not a .cmp file')
    
    # Check if the path is a directory
    elif os.path.isdir(filepath):
        print('The path is a directory. Here are its .cmp files:')
        # Loop through each file in the directory
        for filename in os.listdir(filepath):
            # Check if the file has a .cmp extension
            if filename.endswith('.cmp'):
                # Print the name of the .cmp file
                print(filename)
    
    # Handle the case where the path is neither a file nor a directory
    else:
        print('The specified path does not exist')
else:
    # Inform the user if the path does not exist
    print('Please provide a path.')
