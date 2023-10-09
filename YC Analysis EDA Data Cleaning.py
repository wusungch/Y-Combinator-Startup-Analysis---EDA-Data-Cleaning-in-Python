import pandas as pd
import ast
import matplotlib.pyplot as plt

# merging the two datasets
pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 10)
df1 = pd.read_csv('yc_essential_data.csv')
df2 = pd.read_csv('2023-02-27-yc-companies.csv')
merged_df = pd.merge(df1, df2, left_on='id', right_on='company_id', how='left')

# removing unnecessary/duplicate columns from the merged dataset
columns_to_remove = ['team_size_y', 'website_y', 'long_description_y',
                     'batch_y',
                     'status_y', 'tags_y', 'all_locations', 'company_name',
                     'company_id', 'objectID']
df3 = merged_df.drop(columns=columns_to_remove)

# renaming the column names
col_to_rename = {'website_x': 'website',
                 'long_description_x': 'long_description',
                 'team_size_x': 'team_size',
                 'highlight_latinx': 'highlight_latin',
                 'tags_x': 'tags', 'batch_x': 'batch', 'status_x': 'status'}
df3 = df3.rename(columns=col_to_rename)

# EDA & Data Cleaning
# 1. string splitting of 'location'
# replace NA values with empty string in 'location'
df3['location'].fillna('', inplace=True)
city = df3['location'].apply(lambda x: x.split(',')[0])
state_or_country = df3['location'].apply(
    lambda x: x.split(',')[1] if ',' in x else '')
df3['city'] = city


# find companies that have null value as team size to check if they are still active -- yes, many of them are so should not just replace with 1
null_rows = df3[df3['team_size'].isnull()]
null_company_id = null_rows['id']
# print(null_company_names)

# find companies that have 0 as team_size to check if they are still active -- yes many of them are
zero_rows = df3[df3['team_size'] == 0]
zero_company_id = zero_rows['id']
# print(zero_company_id)

# assumption: replace values where team_size is null with 0
# 2. Replace null values in 'team_size' column with 0s
df3['team_size'].fillna(0, inplace=True)

# 3. Dealing with missing values and data type issues for each column
# replace null values in 'short_description', 'long_description', 'country', 'cb_url', 'linkedin_url' with empty strings,
# 'year_founded' with 0
df3['slug'].fillna('', inplace=True)
df3['one_liner'].fillna('', inplace=True)
df3['demo_day_video_public'].fillna('', inplace=True)
df3['app_answers'].fillna('', inplace=True)
df3['short_description'].fillna('', inplace=True)
df3['long_description'].fillna('', inplace=True)
df3['country'].fillna('', inplace=True)
df3['website'].fillna('', inplace=True)
df3['cb_url'].fillna('', inplace=True)
df3['linkedin_url'].fillna('', inplace=True)
df3['num_founders'].fillna(0, inplace=True)
df3['founders_names'].fillna('', inplace=True)
df3['year_founded'].fillna(0, inplace=True)
df3['year_founded'] = df3['year_founded'].astype(int)

# Dealing with entry errors in 'website'
web = df3['website'].apply(
    lambda x: x.replace('https://', '') if x == 'https://' else x)
df3['website'] = web

# Showing the number of startups belonging to each industry
#print(df3['industry'].value_counts())
#print(df3['num_founders'].value_counts())

################################################################################
# 4. Extracting strings contained in the lists in the 'tags' column
# Converting object data type to a panda series
list_of_lists = df3['tags']
# Converting strings, which Python misidentified, to lists
list_of_lists = list_of_lists.apply(
    lambda x: ast.literal_eval(x) if isinstance(x, str) else x)

# Looping through list_of_lists to extract individual elements and store them in a single list
industries = []
for lst in list_of_lists:
    for element in lst:
        industries.append(element)

unique_industries = []
for item in industries:
    if item not in unique_industries:
        unique_industries.append(item)

# print(unique_industries)
# print(len(unique_industries))

# Dealing with Subcategory Mapping
# find the most common subcategories
def count_unique_values(lst: list):
    unique_counts = {}
    for item in lst:
        if item in unique_counts:
            unique_counts[item] += 1
        else:
            unique_counts[item] = 1
    return unique_counts

count_dict = count_unique_values(industries)

sorted_unique_counts = dict(
    sorted(count_dict.items(), key=lambda item: item[1], reverse=True))
#print(sorted_unique_counts)
#print(sorted_unique_counts.__len__())
# plotting a bar chart with 'category'(key) on the x-axis and 'count'(value) on the y-axis from the dictionary
categories = list(sorted_unique_counts.keys())[:30]
counts = list(sorted_unique_counts.values())[:30]

plt.figure(figsize=(30, 7))  # Set the figure size
plt.bar(categories, counts, color='skyblue')  # Create the bar chart
plt.xlabel('Categories')  # Label for the x-axis
plt.ylabel('Values')  # Label for the y-axis
plt.title('Bar Chart from Dictionary')  # Title of the chart

# Show the plot
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
# plt.show()
################################################################################
# 2. Slicing 'subindustry', only retaining the subindustry
df3['subindustry'] = df3['subindustry'].apply(lambda x: x.split(' -> ')[-1] if ' -> ' in x else 'Unspecified')

# filling null values in 'subindustry' column with Unspecified to ensure they are also presented later on the Dashboard
unspecified_rows = df3[df3['subindustry'] == 'Unspecified']
#print(df3['subindustry'].value_counts())

# Write to .csv
file_path = '/Users/williamwu/Desktop/Tableau/yc directory/cleaned_yc_dataset.csv'
df3.to_csv(file_path)


