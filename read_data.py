import pandas as pd
from pathlib import Path

def read_data():
    data_path = Path(__file__).parents[0] / "my_data"

    #df = pd.read_excel(data_path / "resultat-ansokningsomgang-2024.xlsx", skiprows=5, sheet_name="Tabell 3")

    df = pd.read_csv(data_path/"supahcoolsoft.csv")

    return df

if __name__ == "__main__":
    df = read_data()
    print(df.columns)
    
