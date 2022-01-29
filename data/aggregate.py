import pandas as pd
from pathlib import Path
from api import fetcher
from data import utils

def forming_dataset(*, start_time: str, end_time: str):
    # CONVERTER TO UNIX TIME
    start_dt_dt, start_dt_unix = utils.converter(sample_dt=start_time)
    end_dt_dt, end_dt_unix = utils.converter(sample_dt=end_time)

    fetcher.flights_accessor(start_time=start_dt_unix, end_time=end_dt_unix)

    df = pd.DataFrame(data=flights_json)
    df.drop(labels=['arrivalAirportCandidatesCount', 'estDepartureAirport', 'etc'])

def fixed_dataset():
    flight_list = pd.concat(
        pd.read_csv(file, parse_dates=['firstseen', 'lastseen', 'day'])
        for file in Path('C:\Users\const\Desktop\MIAE_tutorial\MIAEtutorial\data_set').glob('flightlist_*.csv.gz')
    )
    return flight_list
