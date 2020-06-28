import pandas as pd
import matplotlib, matplotlib.pyplot as plt

data = pd.read_csv("us-counties.csv")

county = input("County FIPS: ")
county_data = data.query(f'fips == "{county}"').drop(['county', 'state', 'fips'], axis = 1)

print(county_data)

