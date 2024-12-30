# -*- coding: utf-8 -*-
"""
Created on Tue May 28 15:04:40 2024

@author: Bzikangcrane
"""
import os  # Importing the 'os' module to interact with the operating system

# Prompt the user to input a file path
filepath = input("Please enter the file path: ")

# Print the entered file path for confirmation
print(filepath)

# Check if the entered file path exists
if os.path.exists(filepath):
    print('The path exists')  # Inform the user that the path exists
    
    # Check if the path is a file
    if os.path.isfile(filepath):
        # Split the file path to get the file extension
        _, ext = os.path.splitext(filepath)
        
        # Check if the file is a .csv file
        if ext == '.csv':
            # Open the file in read mode with the correct encoding
            with open(filepath, 'r', encoding='utf-8-sig') as f:
                # Read all the lines in the file
                lines = f.readlines()
                # Print the contents of the file
                print(lines)
        else:
            # Inform the user if the file is not a .csv file
            print('The file is not a .csv file')
    
    # Check if the path is a directory
    elif os.path.isdir(filepath):
        print('The path is a directory. Here are its .csv files:')
        # List all files in the directory and filter for .csv files
        for filename in os.listdir(filepath):
            if filename.endswith('.csv'):
                # Print the name of each .csv file in the directory
                print(filename)
    
    # Handle the case where the path is neither a file nor a directory
    else:
        print('The specified path does not exist')
else:
    # Inform the user that the path does not exist
    print('Please provide a path.')
