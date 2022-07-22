import pandas as pd

read_df = pd.read_csv('al_results_2020.csv', index_col='index', low_memory=False)
df = read_df.drop(columns=['Zscore', 'gender', 'syllabus'])

# drop missing values in dataframe
df = df.dropna()

print(df.columns)

# select series where student was absent
absent_sub1 = df['sub1_r'] == 'Absent'
absent_sub2 = df['sub2_r'] == 'Absent'
absent_sub3 = df['sub3_r'] == 'Absent'
absent_cgt = df['cgt_r'] == 'Absent'
absent_eng = df['general_english_r'] == 'Absent'

# grab only exam subjects column names
exam_cols = ['sub1_r', 'sub2_r', 'sub3_r', 'cgt_r', 'general_english_r']

# series with absence on all exams
all_absent_series = absent_sub1 & absent_sub2 & absent_sub3 & absent_cgt & absent_eng

# new dataframe object valid to next transformations
valid_df = df[~all_absent_series]


