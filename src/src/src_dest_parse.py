import os
import csv

wfile = open("data/src_dest_bmtc.json", 'wt', encoding='utf-8')

src_dest = set()

with open("../data/bmtc data/3.bus_routes.csv", 'rt',
          encoding='utf-8') as file:
    readfile = csv.reader(file, delimiter=',')
    for row in readfile:
        src_dest.add(row[2])
        src_dest.add(row[3])

src_dest = sorted(src_dest)
for item in src_dest:
    wfile.write(item+"\n")