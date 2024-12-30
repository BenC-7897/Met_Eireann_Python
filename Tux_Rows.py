import pandas as pd # Importing the pandas library 
import glob # Importing the glob module 
files = glob.glob('C:/Users/username/Desktop/file folder/data file folder//*.tux') # Use glob to find all the .tux files in the specified directory
dfs = [] # Initialise an empty list to store Data Frames 
for tux in files: # Loop through each .tux file found by glob 
  temp_df = pd.read_csv(tux) # Read the .tux file into a Data Frame using pandas #
  dfs.append(temp_df) # Append the Data Frame to the list of Data Frames 
final_df = pd.concat(dfs, ignore_index = True) # Concatenate all Data Frames in the list into a single Data Frame 
print(f'The total number of rows in the .tux files is {len(final_df)}') # Print the total number of rows in the concatenated Data Frame 
