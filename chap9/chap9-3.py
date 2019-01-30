import csv

with open("chap9/st3.csv","r") as f:
  r = csv.reader(f,delimiter=",")
  for row in r:
    print((",").join(row))