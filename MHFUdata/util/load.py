import pandas as pd
import os

def create_data_frame(csv_file):
    """
        Creates a dataframe from a csv file useing pandas
    """
    df = pd.read_csv(csv_file)

    return df


def insert_df(db):
    for file_name in os.listdir('source_data/MHFU'):
        file_extn = os.path.splitext(file_name)

        if file_extn[1] == ".csv":
            df = create_data_frame(os.path.join('source_data/MHFU', file_name))
    
            for _, row in df.iterrows():
                # Create the data_dict dynamically using column names
                data_dict = {col: row[col] for col in df.columns}
                
                # Use the generic insert_data function from DB_Ops to insert the row
                db.instert_data(file_extn[0], data_dict)