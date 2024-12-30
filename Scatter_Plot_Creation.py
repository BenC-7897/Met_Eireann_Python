import pandas as pd 
import glob 
import os 
import matplotlib.pyplot as plt 
import seaborn as sns 
directory = 'C:/Users/username/Desktop/file folder/file'  # Specify  the directory containing csv files 
DD2023 = glob.glob(os.path.join(directory, '*.csv')) # Get a list of all csv files in the directory 
combinedDD2023 = pd.DataFrame() # Initialise an empty Data Frame to store the combined data #
for csv_file in DD2023: # Read each csv file and concatenate the data 
   df = pd.read_csv(csv_file) 
   combinedDD2023 = pd.concat([combinedDD2023, df]) 
print(combinedDD2023.head()) # Print the combined Data Frame 
combinedDD2023.plot(kind = 'scatter', x = 'humidity', y = 'air_temp') 
plt.xticks(rotation = 90) 
sns.scatterplot(data = combinedDD2023, x = "humidity", y = "air_temp") 
plt.show() 
