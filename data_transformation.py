import pandas as pd

# load csv file into dataframe object
read_df = pd.read_csv('al_results_2020.csv', index_col='index', low_memory=False)

# remove columns: Zscore, gender, syllabus
df = read_df.drop(columns=['Zscore', 'gender', 'syllabus'])

# drop missing values in dataframe
df = df.dropna()

# select series where student was absent
absent_sub1 = df['sub1_r'] == 'Absent'
absent_sub2 = df['sub2_r'] == 'Absent'
absent_sub3 = df['sub3_r'] == 'Absent'
absent_cgt = df['cgt_r'] == 'Absent'
absent_eng = df['general_english_r'] == 'Absent'

# boolean series with absences on all exams
all_absences_series = absent_sub1 & absent_sub2 & absent_sub3 & absent_cgt & absent_eng

# new dataframe object without absence on all exams; ready to next transformations
clean_df = df[~all_absences_series]

# replace invalid days with 0
clean_df = clean_df.replace('Invalid', '0')

# some of numbers characters are incorrect eg. O and I instead 0 and 1
items_to_replace = ['O', 'I']
cols_to_clean = ['birth_day', 'birth_year']

# replace all invalid characters with correct digits
for col in cols_to_clean:
    for item in items_to_replace:
        if item == item[0]:
            clean_df[col] = clean_df[col].apply(lambda x: x.replace(item, '0'))
        elif item == item[1]:
            clean_df[col] = clean_df[col].apply(lambda x: x.replace(item, '1'))

# check if day in month is not greater than 32 and not less than 0
clean_df['birth_day'] = clean_df['birth_day'].astype(int).apply(lambda x: x if (0 < x < 32) else 'unvalid')

# check if student year of birth between 1950 and 2010
clean_df['birth_year'] = clean_df['birth_year'].astype(int).apply(lambda x: x if (1950 < x < 2010) else 'unvalid')

# convert months names to corresponding month number
months_dict = {'January': '01', 'February': '02', 'March': '03', 'April': '04', 'May': '05', 'June': '06',
               'July': '07', 'August': '08', 'September': '09', 'October': '10', 'November': '11', 'December': '12',
               '0': 'unvalid'}

clean_df['birth_month'] = clean_df['birth_month'].apply(lambda key: months_dict[key])

# create birth_date column from concatenation birth_day, birth_month and birth_day columns
clean_df['birth_date'] = clean_df['birth_day'].astype(str) + '-' + clean_df['birth_month'] + '-' + clean_df[
    'birth_year'].astype(str)

# convert birth_date column to date object; incorrect dates displayed as NaT (missing date)
clean_df['birth_date'] = pd.to_datetime(clean_df['birth_date'], format='%d-%m-%Y', errors='coerce')
# remove columns: birth_day, birth_month, birth_year
clean_df = clean_df.drop(columns=['birth_day', 'birth_month', 'birth_year'])
