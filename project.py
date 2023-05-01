import csv
import pandas as pd
import statistics
import numpy as np
import matplotlib.pyplot as plt

with open('World_Happiness_Report.csv') as file:
    data = csv.reader(file)
    header = next(data)

    rows = []
    for row in data:
        rows.append(row)

df = pd.DataFrame(rows, columns=header)


df.describe(include='all')


print(df)
df.isna()
df.info()


df['Year'] = df['Year']. astype(int)


pre_covid = df[(df['Year'] >= 2005) & (df['Year'] <= 2019)]
post_covid = df[(df['Year'] >= 2020) & (df['Year'] <= 2023)]

print(pre_covid)
print(post_covid)


pre_covid.info()
pre_covid['Log GDP Per Capita'].infer_objects()


pre_covid = df[(df['Year'] >= 2005) & (df['Year'] <= 2019)]
post_covid = df[(df['Year'] >= 2020) & (df['Year'] <= 2023)]


pre_covid['Log GDP Per Capita'] = pd.to_numeric(pre_covid['Log GDP Per Capita'])
pre_covid['Log GDP Per Capita'] = np.log10(pre_covid['Log GDP Per Capita'])
grouped = pre_covid.groupby('Country Name')['Log GDP Per Capita'].mean()


pd.set_option('display.max_rows', None)
print(grouped.to_string())


# Plot the mean log GDP per capita by country for the pre-COVID period
plt.bar(grouped.index, grouped.values, width=0.5)
plt.xticks(rotation=90)
plt.xlabel('Country')
plt.ylabel('Mean Log GDP Per Capita')
plt.title('Mean Log GDP Per Capita by Country (Pre-COVID)')
plt.show()
pre_covid = df[(df['Year'] >= 2005) & (df['Year'] <= 2019)]
post_covid = df[(df['Year'] >= 2020) & (df['Year'] <= 2023)]


post_covid['Log GDP Per Capita'] = pd.to_numeric(post_covid['Log GDP Per Capita'])
post_covid['Log GDP Per Capita'] = np.log10(post_covid['Log GDP Per Capita'])
grouped = post_covid.groupby('Country Name')['Log GDP Per Capita'].mean()


pd.set_option('display.max_rows', None)
print(grouped.to_string())


# Plot the mean log GDP per capita by country for the pre-COVID period
plt.bar(grouped.index, grouped.values, width=0.5)
plt.xticks(rotation=90)
plt.xlabel('Country')
plt.ylabel('Mean Log GDP Per Capita')
plt.title('Mean Log GDP Per Capita by Country (Pre-COVID)')
plt.show()
