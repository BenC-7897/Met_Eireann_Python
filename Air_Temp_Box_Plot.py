import pandas as pd 
import os 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 
os.chdir('C:/Users/username/Desktop/file folder/file') # Set the working directory to where the csv files are located
csv_files = [f for f in os.listdir("C:/Users/username/Desktop/file folder/file") if f.endswith('.csv')] # List all csv files in the directory 
print(csv_files) 
dfs = [] # Initialise an empty list to store Data Frames 
for csv in csv_files: # Read each csv file and append the Data Frame to the list 
  df = pd.read_csv(os.path.join("C:/Users/username/Desktop/file folder/file", csv)) 
  dfs.append(df) 
final_df = pd.concat(dfs, ignore_index = True) # Concatenate all Data Frames into one 
plt.figure(figsize=(10,6)) # Create a figure for the plot with a specific size 
sns.boxplot(x = 'month', y = 'air_temp', data = final_df) # Create a boxplot using seaborn 
plt.title('Dundalk 2023 Air Temperature') # Set the title and labels for the plot 
plt.xlabel('Month') 
plt.ylabel('Air Temperature') 
plt.show() # Display the plot 
