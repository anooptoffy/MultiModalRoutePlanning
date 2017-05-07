import os
import csv

wfile = open("data/bus_stops_bmtc.json", 'wt', encoding='utf-8')

src_dest = set()

with open("../data/bmtc data/1.unq_bus_stops.csv", 'rt',
          encoding='utf-8') as file:
    readfile = csv.reader(file, delimiter=',')
    for row in readfile:
        src_dest.add(row[1])

src_dest = sorted(src_dest)
for item in src_dest:
    wfile.write(item+"\n")