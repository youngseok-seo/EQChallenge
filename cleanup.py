import pandas as pd

def cleanup(file):
    """
    Creates a .csv file containing the filtered dataset

    Argument:
        file: .csv file containing the geodata and timest
    Return:
        True for success, False for error
    """
    try:
        df = pd.read_csv(file)
    except:
        print("Please enter a valid .csv file.")
        return False

    # Create dict to keep track of valid requests
    requests = {}
    suspicious = 0
    for index, row in df.iterrows():

        timest = row[' TimeSt']
        latitude = row['Latitude']
        longitude = row['Longitude']

        # Check for suspicious requests and remove if necessary. 
        if timest not in requests:
            requests[timest] = [latitude, longitude]

        elif requests[timest] == [latitude, longitude]:
            suspicious += 1
            df.drop(index, inplace=True)

    df.to_csv(file, index=False)
    print(f"{file} successfully filtered of {suspicious} suspicious records.")
    return True


if __name__ == "__main__":
    sample_file = './DataSample.csv'
    cleanup(sample_file)