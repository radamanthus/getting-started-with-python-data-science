import csv

with open("us-counties.csv", newline='') as infile:
    data = list(csv.reader(infile))

casesIndex = data[0].index("cases")
deathsIndex = data[0].index("deaths")
dateIndex = data[0].index("date")

date = input("Date (yyyy-mm-dd): ")
cases = sum(int(row[casesIndex]) for row in data if row[dateIndex] == date)
deaths = sum(int(row[deathsIndex]) for row in data if row[dateIndex] == date)

print("Cases: " + str(cases))
print("Deaths: " + str(deaths))
