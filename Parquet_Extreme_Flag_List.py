import dask.dataframe as dd # Import the Dask library for parallel computing with DataFrames

file_path = r"C:/Users/username/Desktop/file folder/data folder/data.parquet" # Define the file path to the Parquet file

ddf = dd.read_parquet(file_path) # Read the Parquet file into a Dask DataFrame

lower_threshold = -15 # Define temperature thresholds for filtering
upper_threshold = 40 # Define temperature thresholds for filtering

filtered_ddf = ddf[(ddf['air_temp'] <= lower_threshold) | (ddf['air_temp'] >= upper_threshold)] # Filter the DataFrame to include rows where 'air_temp' is outside the specified thresholds

filtered_df = filtered_ddf.compute() # Compute the filtered Dask DataFrame into a Pandas DataFrame

for index, row in filtered_df.iterrows(): # Iterate over the rows of the filtered Pandas DataFrame
    print(f"Station number {row['stno']} | Date: {row['date']} | Air Temperature: {row['air_temp']:.2f}") # Print the station number, date, and air temperature for each row                                                                                                                                                                                                                               
