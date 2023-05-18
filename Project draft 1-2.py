#!/usr/bin/env python
# coding: utf-8

# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns
# from sklearn.linear_model import LinearRegression
# from sklearn.impute import SimpleImputer
# from sklearn.preprocessing import OneHotEncoder
# from sklearn.preprocessing import LabelEncoder
# 

# df = pd.read_csv('World_Happiness_Report.csv', skiprows=1)
# 
# for index, row in df.iterrows():
#     print(row)

# columns_to_fill = ['Life Ladder', 'Confidence In National Government', 'Log GDP Per Capita', 'Freedom To Make Life Choices', 'Perceptions Of Corruption']
# 
# for column in columns_to_fill:
#     if df[column].isnull().any():
#         df_missing = df[df[column].isnull()]
#         
#         df_clean = df.dropna(subset=[column])
#         
#         X_train = df_clean[['Year']]
#         y_train = df_clean[column]
#         
#         model = LinearRegression()
#         
#         model.fit(X_train, y_train)
#         
#         X_missing = df_missing[['Year']]
#         
#         y_missing = model.predict(X_missing)
#         
#         df.loc[df[column].isnull(), column] = y_missing
# 
# print(df)
# 

# categorical_columns = ['Regional Indicator']
# 
# imputer = SimpleImputer(strategy='most_frequent')
# 
# for column in categorical_columns:
#     if df[column].isnull().any():
#         imputer_column = df[column].values.reshape(-1, 1)
#         
#         imputed_values = imputer.fit_transform(imputer_column)
#         
#         df[column] = imputed_values
# 
# print(df)
# 

# df.info()
# df.isnull().values

# # df.isna().values.sum()
# # df.isna().sum().sum()
# missing_values = df.isnull()
# missing_counts = missing_values.sum()
# print(missing_counts)
# sns.heatmap(missing_values, cmap='viridis')

# df.describe()

# df.columns

# subplot = df[['Life Ladder', 'Confidence In National Government', 'Log GDP Per Capita', 'Freedom To Make Life Choices', 'Perceptions Of Corruption', 'Regional Indicator']]
# print(subplot)

# subplot.columns

# subplot.info()

# sns.pairplot(subplot, hue='Regional Indicator', palette='bright')
# plt.show()

# subplot2 = df[['Life Ladder', 'Confidence In National Government', 'Country Name', 'Year', 'Log GDP Per Capita', 'Freedom To Make Life Choices', 'Perceptions Of Corruption', 'Regional Indicator']]
# print(subplot2)

# subplot2.describe()

# #sns.scatterplot(subplot2, x='Life Ladder', y='Regional Indicator', color='bright')
# 
# 
# sns.scatterplot(data=subplot2, x='Life Ladder', y='Log GDP Per Capita', hue='Regional Indicator', palette='bright')
# plt.title('Happiness vs. GDP by Region')
# plt.xlabel('Life Ladder')
# plt.ylabel('Log GDP Per Capita')
# plt.show()
# 
# 
# plt.show()

# import plotly.express as px
# 
# fig = px.scatter(df, x="gdpPercap", y="lifeExp", color="continent",
#                  size="pop", hover_name="country", log_x=True,
#                  animation_frame="year", range_x=[100, 100000],
#                  range_y=[20, 90], labels={"gdpPercap": "GDP per capita",
#                                           "lifeExp": "Life Expectancy"},
#                  title="Gapminder Visualization")
# fig.update_layout(
#     updatemenus=[
#         dict(
#             type="buttons",
#             buttons=[
#                 dict(
#                     label="Play",
#                     method="animate",
#                     args=[None, {"frame": {"duration": 500, "redraw": True}, "fromcurrent": True, "mode": "immediate"}],
#                 ),
#                 dict(
#                     label="Pause",
#                     method="animate",
#                     args=[[None], {"frame": {"duration": 0, "redraw": False}, "mode": "immediate", "transition": {"duration": 0}}],
#                 ),
#             ],
#         )
#     ],
# )
# fig['layout']['sliders'][0]['currentvalue']['prefix'] = 'Year: '
# fig['layout']['sliders'][0]['currentvalue']['suffix'] = ' '
# 
# fig.update_layout(
#     sliders=[
#         {
#             "active": len(df["year"].unique())-1,
#             "currentvalue": {
#                 "visible": True,
#                 "prefix": "Year: ",
#                 "xanchor": "right"
#             },
#             "steps": [
#                 {
#                     "method": "animate",
#                     "label": year,
#                     "args": [
#                         [year],
#                         {"frame": {"duration": 300, "redraw": False}, "mode": "immediate"}
#                     ],
#                 }
#                 for year in df["year"].unique()
#             ],
#         }
#     ],
# )
# 
# fig.show()
# 

# # df[year] = .year
# # pre_covid = df[df['Year'].isin([2017, 2018, 2019])]
# # post_covid = df[df['Year'].isin([2020, 2021, 2022])]
# print(df.columns)

# In[ ]:




