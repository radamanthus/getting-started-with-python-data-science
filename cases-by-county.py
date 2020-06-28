import csv

with open("us-counties.csv", newline='') as infile:
    data = list(csv.reader(infile))

dateIndex = data[0].index("date")
casesIndex = data[0].index("cases")
deathsIndex = data[0].index("deaths")
fipsIndex = data[0].index("fips")

county = input("County FIPS: ")
rowsForCounty = [row for row in data if row[fipsIndex] == county]

for row in rowsForCounty:
    print("Date: " + row[dateIndex] + ", Cases: " + row[casesIndex] + ", Deaths: " + row[deathsIndex])


