import pandas as pd
import numpy as np
import sys
if len(sys.argv) != 3: # Get the file paths from command line arguments
    print("Usage: python script_name.py <data_file_path> <output_csv_file>")
    sys.exit(1)
file_path = sys.argv[1]
output_csv_file = sys.argv[2]
try: # Read the Parquet file into a DataFrame
    df = pd.read_parquet(file_path, engine='pyarrow')
except FileNotFoundError:
    print(f"File not found: {file_path}")
    sys.exit(1)
lower_threshold = -15 # Define thresholds
upper_threshold = 40 # Define thresholds
thresh = 0.001 # Define thresholds
df['is_extreme'] = ((df['air_temp'] != -99) & ((df['air_temp'] < lower_threshold) | (df['air_temp'] > upper_threshold))) # Flag extreme values (excluding -99)
df['is_missing'] = (pd.isnull(df['air_temp']) | (df['air_temp'] == -99)) # Flag missing values (including -99)
subset_df = df.copy() # Flag stuck sensor values
for i in range(1, 5):
    subset_df[f'temp_shift_{i}'] = subset_df['air_temp'].shift(-i)
subset_df['is_stuck'] = (
    (subset_df['air_temp'] != -99) &
    np.isclose(subset_df['air_temp'], subset_df['temp_shift_1'], atol=thresh) &
    np.isclose(subset_df['temp_shift_1'], subset_df['temp_shift_2'], atol=thresh) &
    np.isclose(subset_df['temp_shift_2'], subset_df['temp_shift_3'], atol=thresh) &
    np.isclose(subset_df['temp_shift_3'], subset_df['temp_shift_4'], atol=thresh)
)
extreme_values_df = df[df['is_extreme']][['stno', 'date', 'air_temp', 'is_extreme']] # Separate DataFrames for extreme, missing and stuck values
missing_values_df = df[df['is_missing']][['stno', 'date', 'air_temp', 'is_missing']] # Separate DataFrames for extreme, missing and stuck values
stuck_sensor_df = subset_df[subset_df['is_stuck']][['stno', 'date', 'air_temp', 'is_stuck']] # Separate DataFrames for extreme, missing and stuck values
extreme_count = extreme_values_df.shape[0] # Count flags
missing_count = missing_values_df.shape[0] # Count flags
stuck_count = stuck_sensor_df.shape[0] # Count flags
summary_df = pd.DataFrame({ # Create a summary DataFrame
'Flag Type': ['Extreme', 'Missing', 'Stuck'],
    'Count': [extreme_count, missing_count, stuck_count]
})
flagged_rows_df = pd.concat([extreme_values_df, missing_values_df, stuck_sensor_df]) # Save flagged rows to the specified CSV file
flagged_rows_df.to_csv(output_csv_file, index=False)
print("\nSummary:") # Display summary in the command prompt
print(f"Extreme flags: {extreme_count}")
print(f"Missing flags: {missing_count}")
print(f"Stuck flags: {stuck_count}")
print("\nFlagged rows saved to:", output_csv_file)
