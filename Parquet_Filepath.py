from pyarrow.parquet import ParquetDataset
path = 'C:/Users/username/Desktop/file folder/ data file folder/file.parquet' # Specify the path to your Parquet Files 
dataset = ParquetDataset(path, use_legacy_dataset = False) # Create a Parquet Dataset
nrows = sum(p.count_rows() for p in dataset.fragments) # Compute the total row count 
print(f'The total number of rows in the Parquet files is {nrows}') 
