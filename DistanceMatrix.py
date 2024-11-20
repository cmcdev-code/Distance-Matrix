import pandas as pd
import googlemaps
from itertools import tee
import yaml
import math
from typing import List
import requests



def generate_distance_matrix_curl(file_in_name: str,key: str,**kwargs)->List[List[float]]:
    """

    Will generate a distance matrix and time matrix from a csv file containing latitude and longitude values

    Args:
        file_in_name: file name of the csv file
    
    Returns:
        List[List[float]]: distance matrix in km i'th and j'th element is the distance between i'th and j'th point travelled via road in km
        List[List[float]]: time matrix in minutes i'th and j'th element is the time taken to travel between i'th and j'th point via road in minutes
    """

    
    distanceMatrix = []
    timeMatrix = []
    df = pd.read_csv(file_in_name)
    for i in range(len(df)):
        distanceMatrix.append([])
        timeMatrix.append([])
        # can call up to 25 points for destination
        for j in range(0,len(df),25):
            url = f"https://maps.googleapis.com/maps/api/distancematrix/json?origins={df.iloc[i]['Latitude']},{df.iloc[i]['Longitude']}&destinations="
            for k in range(j, min(j+25, len(df))):
                url += f"{df.iloc[k]['Latitude']},{df.iloc[k]['Longitude']}|"
            url = url[:-1]
            url += f"&key={keys}"
            response = requests.get(url)
            for k in range(j, min(j+25, len(df))):
                distanceMatrix[i].append(response.json()['rows'][0]['elements'][k-j]['distance']['value']/1000)
                timeMatrix[i].append(response.json()['rows'][0]['elements'][k-j]['duration']['value']/60)
       
 
    if 'distanceFile' in kwargs:
        pd.DataFrame(distanceMatrix).to_csv(kwargs['distanceFile'], index=False,header=False)
        

  
    if 'timeFile' in kwargs:
        pd.DataFrame(timeMatrix).to_csv(kwargs['timeFile'], index=False,header=False)
        

    return distanceMatrix, timeMatrix

if __name__ == "__main__":
    #get the key from the yaml file
    with open("config.yaml", 'r') as stream:
        key = yaml.safe_load(stream)['key']
        input_file = yaml.safe_load(stream)['input_file']
        outputDistFile = yaml.safe_load(stream)['outputDistFile']
        outputTimeFile = yaml.safe_load(stream)['outputTimeFile']
        
        
    generate_distance_matrix_curl("data.csv", key, distanceFile = outputDistFile, timeFile = outputTimeFile)
    