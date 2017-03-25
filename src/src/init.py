import os
import csv
from math import radians, cos, sin, asin, sqrt

'''
data
├── bmrc data
│   └── MetroStation.csv
├── bmtc data
│   ├── 1.unq_bus_stops.csv
│   ├── 1.unq_bus_stops_header.csv
│   ├── 2.bus_stations.csv
│   ├── 2.bus_stations_header.csv
│   └── 3.bus_routes.csv

'''

class MutltiModalRoute:
    ''' Main class for Mutlti Modal Route planning. '''

    def __init__(self):
        self.path = os.listdir("../data/bmtc data")
        self.unique_bust_stops = dict() # dict for storing unique
                                        # bus stops
        self.uniq_bust_routes = dict()
        self.unique_bust_stops_2 = dict() # verification dict()

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

    def main(self):
        ''' Main function  '''
        self.path = sorted(self.path)
        print(self.path)
        with open("../data/bmtc data/"+self.path[0], 'rt',
                  encoding='utf-8') \
                as \
                csvfile:
            readfile = csv.reader(csvfile, delimiter=',')
            #
            # ^^^^^^^data cleaning, some ascii in between utf-8
            # encoded file ^^^^^^^^^
            #
            # UnicodeDecodeError:
            #           'utf-8' codec can't decode byte 0xa0 in position 2980:
            #            invalid start byte
            #
            # Solution:
            #
            # Got rid of the error by opening it in Libre office
            # and saving it as Text CVS format with encoding utf-8
            #
            count = 0
            for row in readfile:
                #print(', '.join(row))
                self.unique_bust_stops[row[1]] = count
                count += 1
        #print(self.path)
        #print(self.unique_bust_stops)
        print(len(self.unique_bust_stops), " Unique bus tops")

        with open("../data/bmtc data/"+self.path[2],'rt',
                  encoding='utf-8') as csvfile:
            readfile = csv.reader(csvfile, delimiter=',')
            count = 0
            for row in readfile:
                #print(', '.join(row))
                if self.uniq_bust_routes.get(row[4]) == None:
                    self.uniq_bust_routes[row[4]] = 1
                else:
                    self.uniq_bust_routes[row[4]] += 1
                self.unique_bust_stops_2[row[3]] = count
                count += 1

        print(len(self.uniq_bust_routes), " Unique routes")
        #print(len(self.unique_bust_stops_2))
        #print(len(self.unique_bust_stops))

        #print(self.uniq_bust_routes)

        #
        # calculate distance between origin and destination
        #

        dis = 0
        with open("../data/bmtc data/"+self.path[2], 'rt',
                  encoding= 'utf-8') as csvfile:
            readfile = csv.reader(csvfile, delimiter = ',')
            count = 0
            for row in readfile:
                #print(row[4])
                if '263P' == row[4]:
                    print(','.join(row))
                else:
                    break

        dis = self.haversine(13.0455367265411,77.5055545144687,13.0408676171254,77.504874711254)
        dis += self.haversine(13.0408676171254,77.504874711254, 13.0386169338844,77.5045504332105)
        dis += self.haversine(13.0386169338844,77.5045504332105, 13.0336009734817,77.5041360893561)
        dis += self.haversine(13.0336009734817,77.5041360893561, 13.0314991383208,77.5035461729168)
        dis += self.haversine(13.0314991383208,77.5035461729168, 13.0276026982709,77.4936370371092)
        dis += self.haversine(13.0276026982709,77.4936370371092,13.0281844260398,77.4895871820463)
        dis += self.haversine(13.0281844260398,77.4895871820463, 13.0293636453365,77.4836860839008)
        dis += self.haversine(13.0293636453365,77.4836860839008, 13.026171634,77.4731424451)
        dis += self.haversine(13.026171634,77.4731424451,13.0216765859596,77.4676410511072 )
        dis += self.haversine(13.0216765859596,77.4676410511072,13.03777311,77.4612450041 )
        dis += self.haversine(13.03777311,77.4612450041, 13.0453056260008,77.4613212145148)
        dis += self.haversine(13.0453056260008,77.4613212145148, 13.0493558943,77.4599098507)
        dis += self.haversine(13.0493558943,77.4599098507,13.0572077681152,77.4601837299526 )
        dis += self.haversine(13.0572077681152,77.4601837299526,13.0606236868,77.461264031 )
        print(dis)
        return



if __name__ == '__main__':
    route = MutltiModalRoute()
    route.main()