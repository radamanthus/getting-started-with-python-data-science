import pandas as pd
import matplotlib, matplotlib.pyplot as plt

data = pd.read_csv("us-counties.csv")

county = input("County FIPS: ")
county_data = data.query(f'fips == "{county}"').drop(['county', 'state', 'fips'], axis = 1)

matplotlib.style.use("ggplot")

plt.plot(county_data['date'], county_data['cases'])
plt.plot(county_data['date'], county_data['deaths'])
plt.show()

