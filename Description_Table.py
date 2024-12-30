import pandas as pd 
import os 
import numpy as np 
import matplotlib.pyplot as plt 
from pandas.plotting import table 
os.chdir('C:/Users/username/Desktop/file folder/file') # Set the working directory 
csv_files = [f for f in os.listdir("C:/Users/username/Desktop/file folder/file") if f.endswith('.csv')] # List all csv files in the directory 
print(csv_files) 
dfs = [] # Read each csv file and concatenate them into a single dataframe 
for csv in csv_files: 
  df = pd.read_csv(os.path.join("C:/Users/username/Desktop/file folder/file", csv))
  dfs.append(df) 
final_df = pd.concat(dfs, ignore_index = True) 
desc = final_df['air_temp'].describe() # Describe the 'air_temp' column 
plot = plt.subplot(111, frame_on = False) # Create a subplot without frame 
plot.xaxis.set_visible(False) # Remove axis 
plot.yaxis.set_visible(False) # Remove axis 
table(plot, desc, loc = 'upper right') # Create the table and position it in the upper right corner 
plt.savefig('desc_plot.png') # Save the plot as a PNG file 
