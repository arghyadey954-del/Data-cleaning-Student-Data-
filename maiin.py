import pandas as pd

#  Load data
df = pd.read_csv('student_data.csv')

print("Original Data:")
print(df)

#  Remove duplicates
df = df.drop_duplicates()

#  Fill missing values with average of column
df['Math'] = df['Math'].fillna(df['Math'].mean())
df['Science'] = df['Science'].fillna(df['Science'].mean())
df['English'] = df['English'].fillna(df['English'].mean())

#  Convert to integer
df['Math'] = df['Math'].astype(int)
df['Science'] = df['Science'].astype(int)
df['English'] = df['English'].astype(int)

#  Create Total column
df['Total'] = df['Math'] + df['Science'] + df['English']

#  Create Grade column
def get_grade(total):
    if total >= 250:
        return 'A'
    elif total >= 200:
        return 'B'
    else:
        return 'C'

df['Grade'] = df['Total'].apply(get_grade)

#  Show cleaned data
print("\nCleaned Data:")
print(df)

#  Save cleaned file
df.to_csv('cleaned_student_data.csv', index=False)

print("\nCleaned file saved!")