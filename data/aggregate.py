import pandas as pd
from pathlib import Path

def fixed_dataset():
    flight_list = pd.concat(
        pd.read_csv(file, parse_dates=['firstseen', 'lastseen', 'day'])
        for file in Path('C:\Users\const\Desktop\MIAE_tutorial\MIAEtutorial\data_set').glob('flightlist_*.csv.gz')
    )
    return flight_list
