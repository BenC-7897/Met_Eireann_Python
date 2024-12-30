import pandas as pd 
import os 
import numpy as np 
import matplotlib.pyplot as plt 
from pandas.plotting import table 
os.chdir('C:/Users/username/Desktop/file folder/file') # Set the working directory to where the csv files are located 
csv_files = [f for f in os.listdir("C:/Users/username/Desktop/file folder/file") if = f.endswith('.csv')] # List all csv files in the directory 
print(csv_files) 
dfs = [] # Initialise an empty list to share Data Frames 
for csv in csv_files: # Iterate over each csv file and read it into a Data Frame 
  df = pd.read_csv(os.path.join("C:/Users/username/Desktop/file folder/file", csv)) 
  dfs.append(df) 
final_df = pd.concat(dfs, ignore_index = True) # Concatenate all Data Frames in the list into a single Data Frame 
grouped = final_df.groupby('month')['air_temp'] # Group by 'month' and calculate summary statistics for 'air_temp' 
summary = grouped.agg(['mean', 'min', 'max']) 
print(summary) 
plot = plt.subplot(111, frame_on = False) # Create a subplot without frame 
plot.xaxis.set_visible(False) # Remove axis from the plot 
plot.yaxis.set_visible(False) # Remove axis from the plot 
table(plot, summary, loc = 'upper right') # Create the table plot and position it in the upper right corner 
plt.savefig('monthly_plot.png') # Save the plot as a PNG file 
