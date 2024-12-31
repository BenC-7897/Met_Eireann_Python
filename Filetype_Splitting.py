import os 
directory = 'C:/Users/username/Desktop/file folder/data file folder/file' # Specify the directory 
files = os.listdir(directory) # Get a list of all files in the directory
cmp_csv_files = [file for file in files if file.endswith('.cmp.csv')] # Filter the list for .cmp.csv files and rename them 
for file in cmp_csv_files: 
  new_name = file{:-4] 
  os.rename(os.path.join(directory,file), os.path.join(directory,new_name)) 
  print(f'Renamed {file} to {new_name}') 
for file in files: # Now process the other files based on their extensions 
  if file.endswith(".cmp"): 
    print(f"Processing .cmp file: {file}") # Add your .cmp file processing code here
  elif file.endswith(".tux"):  
    print(f"Processing .tux file {file}") # Add your .tux file processing code here 
  elif file.endswith(".csv"): 
    print(f"Processing .csv file {file}") # Add your .csv file processing code here 
  else: 
    print(f"Unknown file type {file}") # Add your code for unknown file types here 
