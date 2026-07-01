import pandas as pd
import os

import pandas

def load_raw_data(verbose=False):
    #Load the raw retail sales dataset from the project's data directory.
    # Args:
    #         verbose (bool): If True, displays a preview of the dataset.
    # Returns:
    #    pandas.DataFrame: The loaded sales dataset.
    
    # Construct the relative path to the dataset
    
    data_path = os.path.join("data", "Sales_Dataset.xlsx")
    # Read the Excel file into a DataFrame
    df = pd.read_excel(data_path)
    if verbose:
        print("Data loaded successfully!")
        print(df.head())

    return df 

if __name__ == "__main__":
    # Execute only when this file is run directly
    load_raw_data(verbose=True)