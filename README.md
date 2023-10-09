# Y-Combinator-Startup-Analysis---EDA-Data-Cleaning-in-Python
* This document involves cleaning and analyzing data from Young Companies (YC) by merging two datasets, performing data preprocessing, and exploring key aspects of the dataset.

## Key Skills and Techniques Showcased
### 1. Data Preparation
* Data Merging: Combining two datasets (df1 and df2) using a left join operation based on a common key (company_id) to create a merged_df.
* Column Removal: Removing unnecessary or duplicate columns from the merged dataset (df3) to streamline the analysis.
### 2. Data Cleaning
* Handling Missing Values: Replacing missing values in various columns with appropriate values, such as filling team_size with zeros and handling nulls in columns like slug, one_liner, and year_founded.
* String Manipulation: Splitting and extracting relevant information from the location column to create city and state_or_country columns. Also, cleaning the website column to remove unnecessary elements.
### 3. Exploratory Data Analysis (EDA)
* Tag Extraction: Extracting individual tags from lists stored in the tags column, providing insights into the most common industry categories.
* Data Visualization: Creating a bar chart to visualize the top industry categories based on tag frequencies.
### 4. Subindustry Analysis
* Slicing 'subindustry': Slicing the subindustry column to retain only the subindustry information and handling unspecified subindustries.
### 5. Data Export
* Saving Cleaned Data: Writing the cleaned dataset to a CSV file for further analysis or visualization in tools like Tableau.

## Next Steps
* This code serves as a solid foundation for more advanced analyses, such as predictive modeling or deeper insights into the YC dataset.
* Further analysis and visualization tools like Tableau are used to explore the data. Link to the Tableau dashboard: https://public.tableau.com/app/profile/william.wu8728/viz/YCDashboard_16967608314930/Dashboard1

