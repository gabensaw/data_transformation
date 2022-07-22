import pandas as pd


read_df = pd.read_csv('al_results_2020.csv', index_col='index')
df = read_df.drop(columns= ['Zscore', 'gender', 'syllabus'])

# drop missing values in dataframe
df = df.dropna()

print(df.columns)
