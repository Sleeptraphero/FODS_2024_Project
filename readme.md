# Income Level Analysis Using Census Data

**Bastian Radlmaier / 20.01.075**

## Motivation/Goal

My motivation behind this project is to explore the factors influencing income levels in the dataset. I want to identify key factors of income levels and understand the distribution of income across different groups.

## Questions I Plan to Analyze

1. **How does age impact individuals earning above and below $50K?**
2. **How does education level correlate with income?**
3. **Are there professions that work more than others?**
4. **Are there any significant differences in income based on gender?**
5. **How do race, working hours, and income level correlate with each other?**

## Dataset

The dataset used in this analysis is derived from: [Kaggle - Adult Incomes in the United States](https://www.kaggle.com/datasets/danielbethell/adult-incomes-in-the-united-states?resource=download&select=adult.data)

### Data Quality

- There are no missing values in any of the columns.
- Numerical columns like age, capital gain/loss, and hours per week are of type `int` as they should be.
- There are 24 duplicates in the dataset.

### Describing the Dataset

After cleaning, the dataset has **32,537 rows**, with each entry containing a value, even if it's zero or unknown. 

- **Age**: Ranges from 17 to 90, with an average age of 38.6 years.
- **Education**: Average years of education are 10.1 years.
- **Working Hours**: Most individuals work around 40 hours per week, with an outlier working 99 hours.
- **Education Levels**:
  - 10,494 have completed high school as their highest level.
  - 1,722 have earned a master's degree.
  - 413 have obtained a doctorate.
- **Gender Imbalance**: 21,775 males compared to 10,762 females.
- **Country of Origin**: Predominantly from the United States, with the least common entry from the Netherlands.
- **Income**: 24,698 individuals earn over $50,000, while 7,839 earn less.

## Question Summary/Answers

### How does age impact income?

The plot shows that almost no young adults earn more than $50K. This begins to change just before age 30. Regardless of age, more people earn less than $50K. The peak age for earning above $50K is 44.3, after which the numbers decrease.

### How does education level correlate with income?

Almost no one who finished 12th grade or below earns more than $50K. Starting from high school graduates, this changes, but they remain in the minority. Earning a master's degree appears to be a turning point, with those earning less than $50K becoming the minority. This trend is more pronounced with professional schools and doctorates.

### Are there professions that work more than others?

Based on working hours per week, farmers and fishers work the most at 47 hours, followed by executives and those in transportation. The average is slightly over 40 hours per week. The least hours are worked by those in private household services (32 hours) and administrative tasks (37.6 hours).

### Are there any significant differences in income based on gender?

There are differences in income. Approximately one-third of men earn more than $50,000 per year, whereas only about one-ninth of women do. Additionally, men are represented twice as often as women in the dataset.

### How do race, working hours, and income level correlate with each other?

Across all races, working hours are close to a 40-hour work week. White individuals have a secondary peak at 50 hours, which other groups do not have. Working more hours generally leads to higher income across all ethnicities. Asians and Indians tend to work more hours and earn higher income than other groups.
