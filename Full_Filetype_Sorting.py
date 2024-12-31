import os 
import pandas as pd 
directory = 'C:/Users/username/Desktop/file folder/data file folder/file' # Define the directory containing the data files 
files = os.listdir(directory) # List all files in the specified directory 
csv_dataframe = pd.DataFrame() # Initialise empty Data Frames for different filetypes 
tux_dataframe = pd.DataFrame() # Initialise empty Data Frames for different filetypes
cmp_dataframe = pd.DataFrame() # Initialise empty Data Frames for different filetypes 
cmp_csv_files = [file for file in files if file.endswith('.cmp.csv')] # Filter out files that end with '.cmp.csv' 
for file in cmp_csv_files: # Rename files with the '.cmp.csv' suffix by removing the suffix 
  file_path = os.path.join(directory, file) # Full path to the file 
  new_name = file_path[:-4] # Remove the ('.csv') 
  os.rename(file_path, new_name) # Rename the file 
  print(f"Renamed {file_path} to {new_name}") # Print confirmation message 
for file in files: # Process each file in the directory 
  file_path = os.path.join(directory, file) # Full path to the file 
  if file.endswith('.csv') # Read csv file into Data Frame and concatenate 
    csvdf = pd.read_csv(file_path) 
    csv_dataframe = pd.concat([csv_dataframe, csvdf]) 
  elif file.endswith('.tux') # Read tux file into Data Frame and concatenate 
    tuxdf = pd.read_csv(file_path) 
    tux_dataframe = pd.concat([tux_dataframe, tuxdf]) 
  elif file.endswith('.cmp') # Read cmp file into Data Frame and concatenate 
    cmpdf = pd.read_csv(file_path) 
    cmp_dataframe = pd.concat([cmp_dataframe, cmpdf]) 
print("Data loaded into data frames") # Print confirmation message after loading all data into Data Frames 
csv_dataframe.to_csv('csv_data.csv', index = False) # Save the combined Data Frame to csv files 
tux_dataframe.to_csv('tux_data.csv', index = False) # Save the combined Data Frame to csv files 
cmp_dataframe.to_csv('cmp_data.csv', index = False) # Save the combined Data Frame to csv files  
print("Data Frames saved to csv files") # Print confirmation message after saving Data Frames to csv files 
