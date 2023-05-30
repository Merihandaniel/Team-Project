**World Happiness Report: Exploring the Impact of COVID-19 on Happiness**

Welcome to our project exploring the world of happiness and its potential connection to the COVID-19 pandemic. In this analysis, we delve into the World Happiness Report dataset to investigate whether the global health crisis has had an impact on people's well-being. Our main research question is how did the prevalence of happiness change between the pre-COVID and post-COVID eras in world countries, considering economic and social factors? 

Our primary data source for this project is the World Happiness Report dataset, which we obtained from Kaggle (https://www.kaggle.com/datasets/usamabuttar/world-happiness-report-2005-present), a platform for data science enthusiasts and professionals. The dataset provides valuable insights into happiness scores and various factors contributing to happiness across different countries and years.

##Data: Handling Null Values, Top GDP Countries, and Pre/Post-COVID Split

In order to handle Null values for Regional indicators, such as Eastern Europe...etc, we used linear regression model to perform regression imputation where we learn to predict missing values based on the available data.

'''import re 

#get the unique values that are NA in regional

unique_values = []
df['R_checker'] = df['Regional Indicator'].isnull()

#print(df['R_checker'])

for i,row in df.iterrows():
    #print
    #country = row['Country Name']
    if row['R_checker']==True:
        unique_values.append(row['Country Name'])
    
#values = np.array(unique_values)
holder = np.unique(unique_values)

#print the unique values
print(np.unique(unique_values))'''



For our literature review, we utlizied the following findings:
https://www.scirp.org/journal/paperinformation.aspx?paperid=92906
https://worldhappiness.report/ed/2022/
https://www.worldvaluessurvey.org/WVSContents.jsp






## Conclusion

Our analysis of the World Happiness Report dataset reveals that COVID-19 has impacted happiness levels differently across countries. Several factors contribute to this variation, including cultural differences, the strictness of lockdown measures, cultural values, political factors, and consumerism.

Cultural factors, such as individualistic versus collectivistic cultures, influence the differential impact of the pandemic on happiness. Strictness of lockdown measures and the adaptability of countries' approaches also play a role. Additionally, traditional versus progressive values and political stability impact happiness levels during the pandemic. 

It is important to acknowledge potential biases in the data, including subjective responses and the influence of the government on respondents' answers.

Despite these limitations, our analysis provides valuable insights into the complex relationship between COVID-19 and happiness. Understanding these factors can inform policies and interventions to support well-being during crises.

This project contributes to the broader discourse on happiness and crisis resilience.


