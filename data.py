import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset 
columns = ['age', 'workclass', 'fnlwgt', 'education', 'education-num', 'marital-status', 'occupation', 'relationship', 
           'race', 'gender', 'capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'income']
data = pd.read_csv(r'FODS_2024/adult.data.csv', names=columns, skipinitialspace=True)

# Checking Data Quality - Missing Data - Duplicates - Types - Inspecting Values

print(data.shape)
print(data.isnull().sum())
print(data.duplicated().sum())
print(data.dtypes)
# for column in columns:
#    print(data[column].value_counts())

# Data Cleaning - Removing Duplicates, Replacing "?" valu es, Trimming whitespace, Remove unused column

cleaned_data = data.copy()
cleaned_data = cleaned_data.drop_duplicates()

# Check for unknowns/? and replace them
columns_with_unknowns = []
for column in cleaned_data.columns:
    if cleaned_data[column].dtype == 'object': 
        if '?' in cleaned_data[column].values:
            columns_with_unknowns.append(column)

for column in columns_with_unknowns:
    cleaned_data.loc[:, column] = cleaned_data[column].replace('?', 'Unknown')

# Trim whitespace and standardize capitalization
string_columns = ['workclass', 'education', 'marital-status', 'occupation', 'relationship', 'race', 'gender', 'native-country']
for column in string_columns:
    cleaned_data.loc[:, column] = cleaned_data[column].str.strip()

# Remove unused column 'fnlwgt'
cleaned_data = cleaned_data.drop(columns=['fnlwgt'])

# Explore Data Quality and some descriptive statistics

numerical_columns = ['age', 'education-num', 'capital-gain', 'capital-loss', 'hours-per-week']
numerical_stats = cleaned_data[numerical_columns].describe()

string_columns = ['workclass', 'education', 'marital-status', 'occupation', 'relationship', 'race', 'gender', 'native-country', 'income']
string_stats = {col: cleaned_data[col].value_counts() for col in string_columns}

print("Numerical Descriptive Statistics:")
print(numerical_stats)

print("\nCategorical Descriptive Statistics:")
for col, stats in string_stats.items():
    print(f"\nColumn: {col}")
    print(stats)

print(cleaned_data.head())
        
# Preparing Data

# Calculate mean age Q1

mean_age_below_50k = cleaned_data[cleaned_data['income'] == '<=50K']['age'].mean()
mean_age_above_50k = cleaned_data[cleaned_data['income'] == '>50K']['age'].mean()
palette = sns.color_palette('muted')

# Sort by academic value for Q2
adjusted_education_values = {
    'Some-college': 'College',
    'Assoc-voc': 'Associate ACDM',
    'Assoc-acdm': 'Associate VOC'
}

cleaned_data['education'] = cleaned_data['education'].replace(adjusted_education_values)

education_levels = cleaned_data['education'].unique().tolist()
custom_order = [
    'Preschool', '1st-4th', '5th-6th', '7th-8th', '9th', '10th', '11th', '12th',
    'HS-grad', 'College', 'Associate VOC', 'Associate ACDM', 'Bachelors', 'Masters',
    'Prof-school', 'Doctorate'
]
education_sorted = sorted(education_levels, key=lambda x: custom_order.index(x))

# Calculate avg working hours for plot Q3
occupation_avg_hours = cleaned_data.groupby('occupation')['hours-per-week'].mean().sort_values()

# Question 1: How does age impact individuals earning above and below $50K?
plt.figure(figsize=(12, 8)) 
ax = sns.histplot(
    data=cleaned_data,
    x='age',
    hue='income',
    multiple='stack',
    palette='muted',
    binwidth=5,
)

plt.title('Age Distribution by Income Level', fontsize=16)
plt.xlabel('Age', fontsize=14)
plt.ylabel('Frequency', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)

color_below_50k = palette[0]
color_above_50k = palette[1]

# Mean lines with text
plt.axvline(mean_age_below_50k, color=color_below_50k, linestyle='-', linewidth=1.5, label='Mean Age <=50K')
plt.axvline(mean_age_above_50k, color=color_above_50k, linestyle='-', linewidth=1.5, label='Mean Age >50K')
plt.text(mean_age_below_50k + 1, plt.ylim()[1] * 0.93, f'Mean: {mean_age_below_50k:.1f}', color=color_below_50k, fontsize=10, va='center')
plt.text(mean_age_above_50k + 1, plt.ylim()[1] * 0.93, f'Mean: {mean_age_above_50k:.1f}', color=color_above_50k, fontsize=10, va='center')

plt.legend(title='Income Level', loc='upper right')
plt.figtext(0.5, 0.01, 'This histogram shows the age distribution among individuals earning above and below $50K. '
                        'The plot highlights which age groups are most prevalent in each income category, with mean ages '
                        'indicated by vertical lines.', wrap=True, ha='center', fontsize=12)

# Question 2: How does education level correlate with income?
plt.figure(figsize=(12, 8))
sns.set_palette("muted")

ax = sns.countplot(
    data=cleaned_data,
    y='education',
    hue='income',
    order=education_sorted
)

plt.title('Income Distribution by Education Level', fontsize=16)
plt.xlabel('Frequency', fontsize=14)
plt.ylabel('Education Level', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.legend(title='Income', fontsize=12, title_fontsize=14)
plt.grid(axis='x', linestyle='--', alpha=0.7)

for container in ax.containers:
    ax.bar_label(container, fmt='%d', fontsize=10, padding=3)

plt.subplots_adjust(bottom=0.15)
plt.figtext(0.5, 0.01, 'This barchart counts the frequencey of income above and below 50.000$ across different education levels. '
                        'It provides insights into how educational levels correlates with income.', 
                        wrap=True, ha='center', fontsize=12)

# Question 3: Are there professions that work more than others?
plt.figure(figsize=(14, 8))
plt.plot(occupation_avg_hours.index, occupation_avg_hours.values, marker='o', color='b', label='Average Hours')

overall_avg = cleaned_data['hours-per-week'].mean()
plt.axhline(overall_avg, color='r', linestyle='--', linewidth=1, label='Overall Average')

for i, (occupation, hours) in enumerate(occupation_avg_hours.items()):
    plt.text(i, hours + 0.3, f'{hours:.1f}', ha='center', va='bottom', fontsize=8)

plt.title('Hours worked per week based on Occupation')
plt.xlabel('Occupation')
plt.ylabel('Working hours per Week')
plt.xticks(rotation=45, ha='right')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.subplots_adjust(bottom=0.2)
plt.figtext(0.5, 0.01, 'This linechart shows the average hours worked per week across different occupations. '
                        'It displays the variation in work hours among job roles compared to the overall average.', 
                        wrap=True, ha='center', fontsize=12)



# Question 4: Are there any significant differences in income based on gender?
plt.figure(figsize=(10, 6))
ax = sns.countplot(data=cleaned_data, x='gender', hue='income', palette='muted')
plt.title('Gender Distribution by Income Level')
plt.xlabel('Gender')
plt.ylabel('Frequency')
plt.legend(title='Income')
plt.subplots_adjust(bottom=0.2)
plt.figtext(0.5, 0.01, 'This countplot displays the distribution of income levels by gender. '
                        'Its important to note that twice as much males are recorded.', wrap=True, ha='center', fontsize=12)

for container in ax.containers:
    ax.bar_label(container)

# Question 5: How do race, working hours and income level corelate with eachother?
sns.set_theme(style="whitegrid")

plt.figure(figsize=(14, 8))

sns.violinplot(
    data=cleaned_data,
    x='race',
    y='hours-per-week',
    hue='income',
    split=True,
    palette='muted',
    inner='quartile'  
)

plt.title('Working Hours by Race and Income Level', fontsize=16)
plt.xlabel('Race', fontsize=14)
plt.ylabel('Hours Per Week', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.legend(title='Income Level', loc='upper right', bbox_to_anchor=(0.85, 1), fontsize=12, title_fontsize=14)

plt.figtext(0.5, 0.01, 'This violin plot visualizes the distribution of weekly working hours across different races and income levels. '
                        'It highlights differences between income categories, with quartiles indicated within each violin.', 
                        wrap=True, ha='center', fontsize=12)
plt.show()