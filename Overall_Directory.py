import os # Importing the os module 
import sys # Importing the sys module 
def list_files_by_extension (directory, desired_extension): # Function to list all files in a given directory and it's subdirectories matching an extension
  if os.path.exists(directory): # Check if the specified directory exists 
   for root, dirs, files in os.walk(directory): # Walk through the directory tree 
     for file in files: # Iterate over each file in the current directory 
      if file.lower().endswith(desired_extension.lower()): # Check if the file's extension matches the desired extension 
        print(os.path.join(root, file)) # Print the full path of the matching file 
      else: 
        print(f"The specified directory '{directory}' doesn't exist") # Print an error message if the directory doesn't exist 
if __name__ == "__main__": # Main block to execute when the script is run from the command line 
  if len(sys.argv) ! = 3: # Check if the script received the correct number of arguments 
   print("Usage: python list_files_by_extension.py<directory_path><file_extension>") 
  sys.exit(1) # Exit the script with an error code if the argument count is incorrect 
  directory_path, desired_extension, sys.argv[1], sys.argv[2] # Extract the directory path and desired file extension 
  list_files_by_extension(directory_path, desired_extension) # Call the function to list files with the specified extension 
