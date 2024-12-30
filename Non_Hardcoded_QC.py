import pandas as pd
import numpy as np
import sys
# Get the file paths from command line arguments
if len(sys.argv) != 3:
    print("Usage: python script_name.py <data_file_path> <output_csv_file>")
    sys.exit(1)
file_path = sys.argv[1]
output_csv_file = sys.argv[2]
# Read the Parquet file into a DataFrame
try:
    df = pd.read_parquet(file_path, engine='pyarrow')
except FileNotFoundError:
    print(f"File not found: {file_path}")
    sys.exit(1)
# Define thresholds
lower_threshold = -15
upper_threshold = 40
thresh = 0.001
# Flag extreme values (excluding -99)
df['is_extreme'] = ((df['air_temp'] != -99) & ((df['air_temp'] < lower_threshold) | (df['air_temp'] > upper_threshold)))
# Flag missing values (including -99)
df['is_missing'] = (pd.isnull(df['air_temp']) | (df['air_temp'] == -99))
# Flag stuck sensor values
subset_df = df.copy()
for i in range(1, 5):
    subset_df[f'temp_shift_{i}'] = subset_df['air_temp'].shift(-i)
subset_df['is_stuck'] = (
    (subset_df['air_temp'] != -99) &
    np.isclose(subset_df['air_temp'], subset_df['temp_shift_1'], atol=thresh) &
    np.isclose(subset_df['temp_shift_1'], subset_df['temp_shift_2'], atol=thresh) &
    np.isclose(subset_df['temp_shift_2'], subset_df['temp_shift_3'], atol=thresh) &
    np.isclose(subset_df['temp_shift_3'], subset_df['temp_shift_4'], atol=thresh)
)
# Separate DataFrames for extreme, missing and stuck values
extreme_values_df = df[df['is_extreme']][['stno', 'date', 'air_temp', 'is_extreme']]
missing_values_df = df[df['is_missing']][['stno', 'date', 'air_temp', 'is_missing']]
stuck_sensor_df = subset_df[subset_df['is_stuck']][['stno', 'date', 'air_temp', 'is_stuck']]
# Count flags
extreme_count = extreme_values_df.shape[0]
missing_count = missing_values_df.shape[0]
stuck_count = stuck_sensor_df.shape[0]
# Create a summary DataFrame
summary_df = pd.DataFrame({
'Flag Type': ['Extreme', 'Missing', 'Stuck'],
    'Count': [extreme_count, missing_count, stuck_count]
})
# Save flagged rows to the specified CSV file
flagged_rows_df = pd.concat([extreme_values_df, missing_values_df, stuck_sensor_df])
flagged_rows_df.to_csv(output_csv_file, index=False)
# Display summary in the command prompt
print("\nSummary:")
print(f"Extreme flags: {extreme_count}")
print(f"Missing flags: {missing_count}")
print(f"Stuck flags: {stuck_count}")
print("\nFlagged rows saved to:", output_csv_file)