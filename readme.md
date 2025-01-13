Income Level Analysis Using Census Data

Bastian Radlmaier / 20.01.075

Motivation/Goal

The motivation behind this project is to explore the factors influencing income levels in the dataset, which includes demographic and occupational information. The goal is to identify key determinants of income levels and understand the distribution of income across different groups.

Questions i plan to analyze:

How does age impact individuals earning above and below $50K?
How does education level correlate with income?
What is the distribution of income across different occupations?
Are there any significant differences in income based on gender or race?
How do working hours relate to income levels

The dataset used in this analysis is derived from: https://www.kaggle.com/datasets/danielbethell/adult-incomes-in-the-united-states?resource=download&select=adult.data

Data Quality:
There are no missing values in any of the columns. This indicates completeness in terms of data availabilit
Numerical columns like age, capital gain/loss, hours per week, ... are of type int as they should be.
There are 24 duplicates in the dataset

Describing the Dataset
After cleaning, the dataset has 32537 rows, with each entry containing a value, even if it's zero or unknown. 
The ages of individuals range from 17 to 90, with an average age of 38,6 years. Years of education are on average 10,1 years. Most individuals work around 40 hours per week, although there is an unlikely outlier working 99 hours. Regarding education, 10,494 individuals have completed high school as their highest level, 1,722 have earned a masters degree and only 413 have obtained a doctorate. There is a noticeable gender imbalance, with males accounting for more than double the number of females, 21,775 males compared to 10,762 females. The vast majority of entries list the United States as the country of origin, with the least common entry being from a single individual from the Netherlands. In terms of income, 24698 individuals earn over $50000, while 7839 earn less than $50000 per year.