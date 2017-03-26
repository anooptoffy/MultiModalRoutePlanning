import os
import csv
from math import radians, cos, sin, asin, sqrt, inf
import json
from pprint import pprint

'''
data
├── bmrc data
│   └── MetroStation.csv
├── bmtc data_large
│   ├── 1.unq_bus_stops.csv
│   ├── 1.unq_bus_stops_header.csv
│   ├── 2.bus_stations.csv
│   ├── 2.bus_stations_header.csv
│   ├── 3.bus_routes.csv
│   └── 3.bus_routes_header.csv
├── bmtc data
│   ├── 1.unq_bus_stops.csv
│   ├── 1.unq_bus_stops_header.csv
│   ├── 2.bus_stations.csv
│   ├── 2.bus_stations_header.csv
│   ├── 3.bus_routes.csv
│   └── 3.bus_routes_header.csv

'''

class MutltiModalRoute:
    ''' Main class for Mutlti Modal Route planning. '''

    def __init__(self):
        self.path = os.listdir("../data/bmtc data")
        self.unq_bus_stops = dict() # dict for storing unique
                                        # bus stops
        self.longitude = '' # India 20.5937° N longitude, 78.9629°
        # E latitude
        self.latitude = ''
        self.uniq_bust_routes = dict()
        self.unq_bus_stops_2 = dict() # verification dict()
        self.adj_matrix = []

    def haversine(self, lon1, lat1, lon2, lat2):
        """
        Calculate the great circle distance between two points
        on the earth (specified in decimal degrees)
        """
        # convert decimal degrees to radians
        lon1, lat1, lon2, lat2 = map(radians,
                                     [lon1, lat1, lon2, lat2])

        # haversine formula
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(
            dlon / 2) ** 2
        c = 2 * asin(sqrt(a))
        r = 6371  # Radius of earth in kilometers. Use 3956 for miles
        return c * r

    def create_route_json(self):
        bus_route_name = dict()
        bus_route_origin = dict()
        bus_route_destination = dict()
        json_data = ''
        with open("../data/bmtc data/" + self.path[4], 'rt',
                  encoding='utf-8') as csvfile:
            readfile = csv.reader(csvfile, delimiter=',')
            count = 0
            for row in readfile:
                # print(', '.join(row))
                bus_route_name[row[0]] = 0
                bus_route_origin[row[2]] = 0
                bus_route_destination[row[3]] = 0
                json_data = row[7]
                with open("data_json/" + row[0], 'w') as \
                        outfile:
                    outfile.write(json_data)

        print(len((bus_route_name)))
        print(len(bus_route_origin))
        print(len(bus_route_destination))
        print(json_data)

        return

    def main(self):
        ''' Main function  '''
        self.path = sorted(self.path)

        # read all the bus stops
        with open("../data/bmtc data/" + self.path[0], 'rt',
                  encoding= 'utf-8') as csvfile:
            readfile = csv.reader(csvfile, delimiter = ',')
            count = 0
            for row in readfile:
                #print(', '.join(row))
                self.unq_bus_stops[row[1]] = [count]
                count += 1

        with open("../data/bmtc data/" +  self.path[2],
                  'rt', encoding='utf-8') as csvfile:
            readfile = csv.reader(csvfile, delimiter = ',')
            for row in readfile:
                #print(', '.join(row))
                self.longitude = row[1]
                self.latitude = row[2]
                if self.uniq_bust_routes.get(row[4]) == None:
                    self.uniq_bust_routes[row[4]] = 1
                else:
                    self.uniq_bust_routes[row[4]] += 1
                if len(self.unq_bus_stops[row[3]]) == 1:
                    self.unq_bus_stops[row[3]].append([self.longitude,
                                            self.latitude])


        #for key in self.unq_bus_stops:
            # print("Bus Stop " , key , "ID long latit",
            #       self.unq_bus_stops[key])
            # print(self.unq_bus_stops[key][0])
            # print(self.unq_bus_stops[key][1])

        print(self.unq_bus_stops['8th mile t dasarahalli 8th mile '
                                 'beside a.k.scooter works'][1])
        print(self.uniq_bust_routes)


        for mat in range(len(self.unq_bus_stops)):
            row = []
            for r in range(len(self.unq_bus_stops)):
                row.append(inf)
            self.adj_matrix.append(row)

        # adding paths to the adjacency matrix
        with open("../data/bmtc data/" + self.path[2], 'rt',
                  encoding='utf-8') as csvfile:
            readfile = csv.reader(csvfile, delimiter=',')
            prev_route = 0
            next_route = 1
            prev_stop = 0
            next_stop = 1
            count = 0
            for row in readfile:
                next_route = row[4]
                next_stop = row[3]
                if prev_route == next_route:
                    long1 = float(self.unq_bus_stops[
                                      prev_stop][1][0])
                    latit1 = float(self.unq_bus_stops[
                                       prev_stop][1][1])
                    long2 = float(self.unq_bus_stops[
                                      next_stop][1][0])
                    latit2 = float(self.unq_bus_stops[
                                       next_stop][1][1])
                    self.adj_matrix[self.unq_bus_stops[prev_stop][0]][
                        self.unq_bus_stops[next_stop][0]] = self.haversine(long1, latit1,
                                                     long2, latit2)

                    self.adj_matrix[self.unq_bus_stops[next_stop][0]][
                        self.unq_bus_stops[prev_stop][0]] = self.haversine(
                        long1, latit1,
                                                     long2, latit2)
                    prev_stop = row[3]

                else:
                    prev_route = row[4]
                    prev_stop = row[3]


        # verification
        print(self.adj_matrix[self.unq_bus_stops['8th mile t dasarahalli 8th mile '
                                 'beside a.k.scooter works'][0]][self.unq_bus_stops['rukmini nagara rukmini nagara beside open area'][0]])
        print(self.adj_matrix[self.unq_bus_stops['rukmini nagara rukmini nagara beside open area'][0]][self.unq_bus_stops['8th mile t dasarahalli 8th mile beside a.k.scooter works'][0]])

        print(self.haversine(float(self.unq_bus_stops['8th mile t '
                                                 'dasarahalli 8th mile '
                                 'beside a.k.scooter works'][1][
                                       0]), float(self.unq_bus_stops[
            '8th mile t dasarahalli 8th mile '
                                 'beside a.k.scooter works'][1][1]),
                             float(self.unq_bus_stops['rukmini '
                                                      'nagara '
                                                'rukmini nagara '
                                                'beside open '
                                                'area'][1][0]),
                             float(self.unq_bus_stops['rukmini '
                                                      'nagara '
                                                'rukmini nagara '
                                                'beside open '
                                                'area'][1][1])))
if __name__ == '__main__':
    route = MutltiModalRoute()
    #route.create_route_json() # call only once
    route.main()