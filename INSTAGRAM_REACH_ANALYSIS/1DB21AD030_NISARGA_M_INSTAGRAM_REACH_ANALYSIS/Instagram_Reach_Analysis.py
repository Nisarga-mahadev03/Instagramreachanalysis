# Analyzing the reach of Instagram account by importing the necessary Python libraries and the dataset.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

#1. Read the data from the csv file
dataset = pd.read_csv("Instagram data.csv", encoding = 'latin1')
print(dataset)
print()
dataFrame =pd.DataFrame(dataset)
print(dataFrame)

#2. Check for null / NaN values and drop if you find any
print(dataset.isnull())
print(dataset.isnull().sum())
print()
#there is no null values

#3. Analyze the distribution of impressions received from home and display it using the distplot of seaborn.
plt.figure(figsize=(10, 10))
plt.style.use('fivethirtyeight')
plt.title("Distribution of Impressions from Home")
sns.distplot(dataset['From Home'])
plt.show()
print()

#4. Analyze the distribution of the impressions received from hashtags and display it using the distplot of seaborn.
plt.figure(figsize=(10, 10))
plt.title("Distribution of Impressions from Hashtags")
sns.distplot(dataset['From Hashtags'])
plt.show()
print()

#5. Analyze the distribution of the impressions received from the explore section and display it using the distplot of seaborn.
plt.figure(figsize=(10, 10))
plt.title("Distribution of Impressions from Explore")
sns.distplot(dataset['From Explore'])
plt.show()
print()

#6. Analyze the percentage of impressions received from various sources and display it as pie chart.
home = dataset["From Home"].sum()
hashtags = dataset["From Hashtags"].sum()
explore = dataset["From Explore"].sum()
other = dataset["From Other"].sum()
Saves = dataset["Saves"].sum()
Comments = dataset["Comments"].sum()
Shares = dataset["Shares"].sum()
Likes = dataset["Likes"].sum()
Profile_Visits = dataset["Profile Visits"].sum()
Follows = dataset["Follows"].sum()
labels = ['From Home', 'From Hashtags', 'From Explore', 'Other','From Saves','From Comments','From Shares',"From Likes","From Profile Visits","From Follows"]
values = [home, hashtags, explore, other,Saves,Comments,Shares,Likes,Profile_Visits,Follows]

fig = px.pie(dataset, values=values, names=labels,
             title='Impressions on Instagram Posts From Various Sources', template='plotly_dark')
fig.update_traces(pull=[0.1, 0, 0, 0])
fig.show()
print()

#7. Create a wordcloud of the caption column to look at the most used words in the caption of Instagram posts.
text = " ".join(i for i in dataset.Caption)
stopwords = set(STOPWORDS)
wordcloud = WordCloud(stopwords=stopwords, background_color="white").generate(text)
plt.figure(figsize=(10, 10))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
print()

#8. Create a wordcloud of the hashtags column to look at the most used hashtags in Instagram posts.
text = " ".join(i for i in dataset.Hashtags)
stopwords = set(STOPWORDS)
wordcloud = WordCloud(stopwords=stopwords, background_color="yellow").generate(text)
plt.figure(figsize=(10, 10))
plt.imshow(wordcloud, interpolation='blackman')
plt.axis("off")
plt.show()
print()

#9. Analyze the relationship between the number of likes and the number of impressions on Instagram posts and display it as scatter chart.
figure_1 = px.scatter(dataFrame, x="Impressions",
                    y="Likes", size="Likes", trendline="ols",
                    title = "Relationship Between Likes and Impressions")
figure_1.show()
print()

#10. Analyze the relationship between the number of comments and the number of impressions on Instagram posts and display it as scatter chart.
figure_2 = px.scatter(dataFrame, x="Impressions",
                    y="Comments", size="Comments", trendline="ols",
                    title = "Relationship Between Comments and Total Impressions")
figure_2.show()
print()

#11. Analyze the relationship between the number of shares and the number of impressions and display it as scatter chart.
figure_3 = px.scatter(dataFrame, x="Impressions",y="Shares",
                    size="Shares", trendline="ols",
                    title = "Relationship Between Shares and Total Impressions")
figure_3.show()
print()

#12. Analyze the relationship between the number of saves and the number of impressions and display it as scatter chart.
figure_4 = px.scatter(dataFrame, x="Profile Visits",
                    y="Follows", size="Follows", trendline="ols",
                    title = "Relationship Between Profile Visits and Followers Gained")
figure_4.show()