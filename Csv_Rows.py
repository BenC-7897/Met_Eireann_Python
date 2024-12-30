import pandas as pd # Importing the pandas library 
import glob # Importing the glob module 
files = glob.glob('C:/Users/username/Desktop/file folder/data file folder/file, *.csv') # Use glob to find all .csv files in the specified directory 
dfs = [] # Initialise an empty list to store Data Frames 
for csv in files: # Loop through each .csv file found by glob 
   temp_df = pd.read_csv(csv) # Read the .csv file into a Data Frame 
   dfs.append(temp_df) # Append the Data Frame to the list of Data Frames 
final_df = pd.concat(dfs, ignore_index = True) # Concatenate all Data Frames in the list into a single Data Frame 
print(f'The total number of rows in the .csv files is {len(final_df)}') # Print the total number of rows in the concatenated Data Frame 
