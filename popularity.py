import numpy as np

def popularity(analysis):
    """
    Argument:
        analysis: dictionary with the same structure as created in analysis.py (POI: [avg, std, rad, den])
    Return:
        dictionary containing the popularity rating from -10 to 10 for each POI 
    """

    # Base the scale off of the mean among POIs. 

    raw_dist = []
    raw_den = []
    for _, value in analysis.items():
        raw_dist.append(value[0])
        raw_den.append(value[3])

    mean_distance = np.mean(raw_dist)
    mean_density = np.mean(raw_den)

    min_distance = np.min(raw_dist)
    max_distance = np.max(raw_dist)

    min_density = np.min(raw_den)
    max_density = np.max(raw_den)

    # Rate each POI on average distance from requests and density. Lower distance and higher density result in a higher rating.
    # Calculate separate scores for distance and density, from -10 to 10. 
    # The largest/smallest values receive +/- 10 to ensure every POI to have a rating.
    # Average distance less than the mean receives a (+) rating, and greater than the mean a (-) rating; precisely on the mean receives a 0.
    # Density greater than the average receives a (+) rating, and less than the mean a (-) rating; precisely on the mean receives a 0.

    # Take the difference between the point and the mean value, and map it between +/- 0-10.
    # (difference between point and mean) / (difference between max/min and mean) * (10)
    # Average the two scores from distance and density to arrive at a final score.

    # Details and other assumptions made found in bonus.txt.

    ratings = {}
    for key, value in analysis.items():
        dist = value[0]
        den = value[3]

        diff_dist = mean_distance - dist # to ensure smaller distance receives a positive rating
        if diff_dist > 0:
            r_dist = (diff_dist / (mean_distance - min_distance)) * 10
        else:
            r_dist = (diff_dist / (max_distance - mean_distance)) * 10
        
        diff_den = den - mean_density # to ensure larger density receives a positive rating
        if diff_den > 0:
            r_den = (diff_den / (max_density - mean_density)) * 10
        else:
            r_den = (diff_den / (mean_density - min_density)) * 10

        r = (r_dist + r_den) / 2

        ratings[key] = r

    return ratings
