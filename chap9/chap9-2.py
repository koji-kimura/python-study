import csv

with open("chap9/st3.csv","w") as f:
  w = csv.writer(f,delimiter=",")
  w.writerow(["one","two","three"])
  w.writerow(["four","five","six"])