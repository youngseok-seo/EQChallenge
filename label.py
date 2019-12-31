import pandas as pd
import numpy as np

def label(file):
    """
    Assigns nearest POI to each request 
    
    Argument:
        file: input .csv file 
    Return:
        True for success, False for error
    """

    try:
        df = pd.read_csv(file)
    except:
        print("Please enter a valid .csv file.")
        return False

    # create dataframe 
    df = pd.read_csv(file)

    # populate a dict to store POIs
    poi_dict = {}
    poi = pd.read_csv('./POIList.csv')
    for _, row in poi.iterrows():
        id = row['POIID']
        lat = row[' Latitude']
        lon = row['Longitude']

        poi_dict[id] = [lat, lon]

    # assign each request to a POI
    poi_list = []
    dist_list = []
    for _, row in df.iterrows():
        lat = row['Latitude']
        lon = row['Longitude']

        poi = None
        min_dist = 999999
        # NOTE: POI1 and POI2 seem to be identical; default to POI1.
        for id, loc in poi_dict.items():
            distance = distanceTo(lat, lon, loc[0], loc[1])
            if distance < min_dist:
                min_dist = distance
                poi = id

        poi_list.append(poi)
        dist_list.append(min_dist)

    # add columns of POIs and distances to dataframe         
    df['POI'] = pd.Series(poi_list).values
    df['Distance'] = pd.Series(dist_list).values

    df.to_csv('./DataSample.csv', index=False)
    print(f"{file} successfully assigned.")
    return True


def distanceTo(sample_lat, sample_lon, poi_lat, poi_lon):
    """
    Helper to calculate distance using Pythagoras
    """

    dx = int(poi_lat) - int(sample_lat)
    dy = int(poi_lon) - int(sample_lon)

    distance = np.sqrt((dx**2) + (dy**2))

    return distance


if __name__ == "__main__":
    sample_file = './DataSample.csv'
    label(sample_file)