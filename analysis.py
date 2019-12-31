import pandas as pd
import numpy as np

def analysis(poi_file, sample_file):
    """
    Argument:
        poi_file: POI list .csv file
        sample_file: sample data .csv file
    Return:
        Dictionary containing list of avg, std, radius and density for each POI
    """

    # In general applications, minimum distance calculation and POI selection for each request
    # would be executed here. However, as it was done in label.py, I will be assuming that
    # the sample data file already has a POI and the distance assigned to each request.

    # As described in label.py, the given POIList.csv contains two of the same POIs (1 & 2).
    # In minimum distance calculations, the requests closest to POI1 and POI2 were assigned 
    # by default to POI1. However, as it cannot be determined simply from the dataset whether 
    # there are two points of interest in the same location or it is a flaw in the data, I will
    # keep both POIs (i.e. they will have identical analysis values).

    poi_df = pd.read_csv(poi_file)
    # initialize dictionary to store raw distance data for each POI
    requests = {}
    for _, row in poi_df.iterrows():
        requests[row['POIID']] = []

    data_df = pd.read_csv(sample_file)
    # populate the dictionary using previously assigned data
    for _, row in data_df.iterrows():
        requests[row['POI']].append(int(row['Distance']))

    # analyze data and store in a new dictionary
    analysis = {}
    for key, value in requests.items():

        # quick fix for a case where POI2 should not be excluded
        if key == 'POI2':
            value = requests['POI1']

        avg = np.mean(value) 
        std = np.std(value)
        rad = np.max(value)
        den = len(value)/(np.pi * (rad**2))

        analysis[key] = [avg, std, rad, den]

        print(f'{key} | avg: {avg}, std: {std}, radius: {rad}, density: {den}')

    return analysis

if __name__ == "__main__":
    poi_file = './POIList.csv'
    sample_file = './DataSample.csv'
    analysis(poi_file, sample_file)