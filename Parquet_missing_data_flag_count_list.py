# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 12:09:25 2024

@author: Bzikangcrane
"""
# Import the Dask library for parallel computing with DataFrames
import dask.dataframe as dd

# Define the file path to the Parquet file
file_path = r"C:/Users/bzikangcrane/Desktop/Met Eireann Data/Database_Project/camp_temp_1min_non_qc_2024.parquet"

# Read the Parquet file into a Dask DataFrame
ddf = dd.read_parquet(file_path)

# Filter the DataFrame to get rows where 'air_temp' is missing (NaN)
missing_data_ddf = ddf[ddf['air_temp'].isnull()]

# Compute the filtered Dask DataFrame into a Pandas DataFrame
missing_data_df = missing_data_ddf.compute()

# Get the number of rows with missing 'air_temp' values
missing_data_count = missing_data_df.shape[0]

# Print the total number of missing 'air_temp' values
print(f"Total missing values in air_temps: {missing_data_count}")

# Iterate over each row in the Pandas DataFrame with missing 'air_temp' values
for index, row in missing_data_df.iterrows():
    # Print the station number and date for each row with missing 'air_temp'
    print(f"Station number {row['stno']} | Date: {row['date']}")