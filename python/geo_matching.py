

import pandas as pd
from shapely.geometry import Point, Polygon

filepath = "/Users/ameinert/python_projects/tier/data/"
filename_rides = "rides_all_2020_01_29.pkl"
filename_stations = "haltestellen.csv"


rides = pd.read_pickle(filepath + filename_rides)
stations = pd.read_csv(filepath + filename_stations)


rides.info()

rides["end_point_lat"], rides["end_point_long"] = rides["end_point"].str.split(",").str
rides["start_point_lat"], rides["start_point_long"] = rides["start_point"].str.split(",").str


rides["date_time"].astype(str) + "_" + rides["vehicle_id"].astype(str)
rides["ID"] = rides["date_time"].astype(str) + "_" + rides["vehicle_id"].astype(str)
rides = rides.set_index("ID")


import time

seconds = time.time()

matchtable = pd.DataFrame(columns=["Haltestelle", "Ride_ID"])

point_buffer = 0.0013652930088452135

for ride in rides.itertuples():

    ride_start_geopoint = Point(float(ride.start_point_lat), float(ride.start_point_long))
    # ride_end_geopoint = Point(float(ride.end_point_lat), float(ride.end_point_long))
    for haltestelle in stations.itertuples():

        haltestelle_point = Point(haltestelle.lat, haltestelle.long)

        if (haltestelle_point.buffer(point_buffer).contains(ride_start_geopoint)):
            # print(haltestelle.Haltestelle + " " + str(ride.Index))

            matchtable = matchtable.append({"Haltestelle": haltestelle.Haltestelle, "Ride_ID": ride.Index}, ignore_index=True)


print("Seconds since epoch =", seconds)