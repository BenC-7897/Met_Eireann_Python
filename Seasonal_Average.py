import pandas as pd 
import glob 
import os 
import matplotlib.pyplot as plt
from pandas.plotting import table 
directory = 'C:/Users/username/Desktop/file folder/file' # Specify the directory containing csv files 
DD2023 = glob.glob(os.path.join(directory, '*.csv')) # Get a list of all csv files in the directory 
combinedDD2023 = pd.DataFrame() # Initialise an empty DataFrame to store the combined data 
for csv_file in DD2023: # Read each csv file and concatenate the data 
  df = pd.read_csv(csv_file) 
  combinedDD2023 = pd.concat([combinedDD2023, df])
combinedDD2023["date"] = pd.to_datetime(combinedDD2023["date"]) # Convert the date column to datetime format 
def season(x): # Define a function to determine the season based on month 
  if x in [3,4,5]: 
   return 'Spring' 
  elif x in [6,7,8]: 
   return 'Summer' 
  elif x in [9,10,11]: 
   return 'Autumn' 
  else 
   return 'Winter' 
comninedDD2023['season'] = combinedDD2023["date"].dt.month.apply(lambda x: season(x)) # Create a new column for season 
group = combinedDD2023.groupby('season')['air_temp'].agg(['mean', 'min', 'max']) # Group by season and calculate mean, minimum and maximum temperatures 
group = group.reindex(index=['Spring', 'Summer', 'Autumn', 'Winter']) 
figure, ax = plt.subplots(figsize=(8,4)) # Create a table and display it 
tbl = table(ax, group, loc = "center", cellloc = "center", colwidths = [0.1]*len(group.columns)) 
tbl.auto_set_font_size(False) 
tbl.set_fontsize(14) 
tbl.scale(2,2) 
plt.show() # Show the table 
