import pandas as pd
import kagglehub
from kagglehub import KaggleDatasetAdapter
from pathlib import Path

def read_data():

    data_path = Path(__file__).parents[0] / "my_data"

    #df = pd.read_excel(data_path / "resultat-ansokningsomgang-2024.xlsx", skiprows=5, sheet_name="Tabell 3")

    df = pd.read_csv(data_path/"supahcoolsoft.csv")

    return df

def read_pisa_data():

    data_path = Path(__file__).parents[0] / "my_data"

    df = pd.read_csv(data_path/"OECD PISA data.csv")

    return df

# if __name__ == "__main__":
#     df = read_data()
#     pisa_df = read_pisa_data()
#     print(df.columns)

#     print("First 5 records:", pisa_df.head())