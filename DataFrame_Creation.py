import pandas as pd 
import os 
import numpy as np 
os.chdir('C:/Users/username/Desktop/file folder/file') # Set the working directory to the location where csv files are stored
csv_files = [f for f in os.listdir("C@/Users/username/Desktop/file folder/file") if f.endswith('.csv')] # List all csv files in the directory 
print(csv_files) # Print the list of csv files to verify the files being processed 
dfs = [] # Initialise an empty list to store Data Frames 
for csv in csv_files: # Iterate over each csv file 
   df = pd.read_csv(os.path.join("C:/Users/username/Desktop/file folder/file", csv)) # Read the csv file into Data Frame 
   dfs.append(df) # Append the Data Frame to the list 
final_df = pd.concat(dfs, ignore_index = True) # Concatenate all Data Frames in the list into a single Data Frame 
