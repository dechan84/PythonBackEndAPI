# Sample of read and w csv files

import csv
with open("SampleCSV.csv") as csvFile:
    csvReader = csv.reader(csvFile, delimiter=",")
    # print(list(csvReader))
    names = []
    stats = []
    for row in csvReader:
        names.append(row[0])
        stats.append(row[1])
csvFile.close()

print(names)
print(stats)

# Know the index of the element name in a list
Index = names.index('Sam')
print(Index)

loanstatus = stats[Index]
print('Sam loan status is '+loanstatus)

# Write values to csv, using w writes completely new file, a is append something to the file
with open("SampleCSV.csv", "a") as wFile:
    writeobject = csv.writer(wFile)
    # writerow accepts list
    writeobject.writerow(["Bob", "rejected"])
wFile.close()