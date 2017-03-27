import os
import csv
import pickle
import collections
from collections import OrderedDict

# wfile = open("data/bus_stops_routes_bmtc.json", 'wt',
#              encoding='utf-8')

src_dest_cord = dict()
src_dest = dict()

with open("../data/bmtc data/2.bus_stations.csv", 'rt',
          encoding='utf-8') as file:
    readfile = csv.reader(file, delimiter=',')
    for row in readfile:
        if row[3] in src_dest.keys():
            src_dest[row[3]].append(row[4])
        else:
            src_dest[row[3]] = [row[4]]
            src_dest_cord[row[3]] = [row[1], row[2]]

src_dest = OrderedDict(sorted(src_dest.items()))
src_dest_cord = OrderedDict(sorted(src_dest_cord.items()))
# print(src_dest_cord)

pickle.dump(src_dest, open("data/bus_stops_routes_bmtc.json", 'wb'))
pickle.dump(src_dest_cord, open("data/bus_stops_loc.json", 'wb'))

#
# for key in src_dest.keys():
#     wfile.write(key+","+",".join(src_dest[key])+"\n")