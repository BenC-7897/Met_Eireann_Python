import dask.dataframe as dd # Import the Dask library for parallel computing with DataFrames

file_path = r"C:/Users/username/Desktop/file folder/data folder/file.parquet" # Define the file path to the Parquet file

ddf = dd.read_parquet(file_path) # Read the Parquet file into a Dask DataFrame

missing_data_ddf = ddf[ddf['air_temp'].isnull()] # Filter the DataFrame to get rows where 'air_temp' is missing (NaN)

missing_data_df = missing_data_ddf.compute() # Compute the filtered Dask DataFrame into a Pandas DataFrame

missing_data_count = missing_data_df.shape[0] # Get the number of rows with missing 'air_temp' values

print(f"Total missing values in air_temps: {missing_data_count}") # Print the total number of missing 'air_temp' values

for index, row in missing_data_df.iterrows(): # Iterate over each row in the Pandas DataFrame with missing 'air_temp' values
    print(f"Station number {row['stno']} | Date: {row['date']}") # Print the station number and date for each row with missing 'air_temp'
