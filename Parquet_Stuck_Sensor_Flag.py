import pandas as pd
import numpy as np

file_path = 'C:/Users/username/Desktop/file folder/data folder/file.parquet' # Define the path to the parquet file

df = pd.read_parquet(file_path, engine='pyarrow') # Read the parquet file into a pandas DataFrame

subset_df = df.head(12955738) # Select a subset of the data 

selected_columns = ['air_temp', 'stno', 'date'] # Extract relevant columns
subset_df = subset_df[selected_columns]

thresh = 0.001 # Define the threshold for determining "stuck" sensors

subset_df['temp_shift_1'] = subset_df['air_temp'].shift(-1) # Create lagged temperature columns
subset_df['temp_shift_2'] = subset_df['air_temp'].shift(-2) 
subset_df['temp_shift_3'] = subset_df['air_temp'].shift(-3)  
subset_df['temp_shift_4'] = subset_df['air_temp'].shift(-4)  

subset_df['is_stuck'] = ( # Identify "stuck" sensors based on the threshold
    np.isclose(subset_df['air_temp'], subset_df['temp_shift_1'], atol=thresh) &
    np.isclose(subset_df['temp_shift_1'], subset_df['temp_shift_2'], atol=thresh) &
    np.isclose(subset_df['temp_shift_2'], subset_df['temp_shift_3'], atol=thresh) &
    np.isclose(subset_df['temp_shift_3'], subset_df['temp_shift_4'], atol=thresh)
)

stuck_info = subset_df[subset_df['is_stuck']][['stno', 'date', 'air_temp']] # Extract information about "stuck" sensors

stuck_info_columns = ['Station Number', 'Date', 'Air Temperature'] # Rename columns for better readability
stuck_info.columns = stuck_info_columns

stuck_info.to_csv('reformed_stuck_sensor_results.csv', index=False) # Save the results to a CSV file

print("Results saved to reformed_stuck_sensor_results.csv") # Print a message to confirm the file save location
