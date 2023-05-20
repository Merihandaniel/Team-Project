# sunburst plot for all
import plotly.express as px

fig = px.sunburst(
    df,
    path=['Country Name', 'Regional Indicator', 'Year'],
    values='Life Ladder',
    color='Log GDP Per Capita',
    color_continuous_scale='Blues',
    hover_name='Country Name',
    hover_data=['Life Ladder', 'Log GDP Per Capita'],
    title='Life Ladder and Log GDP Per Capita by Country, Regional Indicator, and Year'
)

fig.show()

# bar plots for countries
import plotly.express as px

countries = ['India', 'Pakistan', 'Bangladesh']
columns = ['Life Ladder', 'Confidence In National Government', 'Log GDP Per Capita', 'Freedom To Make Life Choices',
           'Perceptions Of Corruption']

for country in countries:
    country_data = pre_asia[pre_asia['Country Name'] == country]

    country_data = country_data.melt(id_vars='Country Name', value_vars=columns, var_name='Indicator',
                                     value_name='Value')

    fig = px.bar(country_data, x='Indicator', y='Value', title=f"Bar Plot for {country}")

    fig.show()

