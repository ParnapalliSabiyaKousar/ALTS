import csv
with open('data.csv','rt')as f :
    data=csv.reader(f)
    #reader function to generate a reader object
    for row in data:
        print(row)
