# Import the Dask library for parallel computing with DataFrames
import dask.dataframe as dd

# Define the file path to the Parquet file
file_path = r"C:/Users/username/Desktop/file folder/data folder/data.parquet"

# Read the Parquet file into a Dask DataFrame
ddf = dd.read_parquet(file_path)

# Define temperature thresholds for filtering
lower_threshold = -15
upper_threshold = 40

# Filter the DataFrame to include rows where 'air_temp' is outside the specified thresholds
filtered_ddf = ddf[(ddf['air_temp'] <= lower_threshold) | (ddf['air_temp'] >= upper_threshold)]

# Compute the filtered Dask DataFrame into a Pandas DataFrame
filtered_df = filtered_ddf.compute() 

# Iterate over the rows of the filtered Pandas DataFrame
for index, row in filtered_df.iterrows():
    # Print the station number, date, and air temperature for each row
    print(f"Station number {row['stno']} | Date: {row['date']} | Air Temperature: {row['air_temp']:.2f}")                                                                                                                                                                                                                               
