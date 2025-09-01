# %%
from bs4 import SoupStrainer, BeautifulSoup
import pandas as pd
import io
import re

# %%
# Transform HTML into single DataFrame

try:
    with open('../html/output.html', 'r') as f:
        html = f.read()
    soup = BeautifulSoup(html, features='lxml')

except FileNotFoundError as e:
    print('output.html not found, run fetch_finals_schedule tool')

tables = soup.find_all('table')
dfs = []
for table in tables:
    df = pd.read_html(io.StringIO(str(table)))[0]

    caption = table.find('caption')
    caption = caption.text.strip() if caption else None
    df['Finals Day'] = caption

    dfs.append(df)

df = pd.concat(dfs)
df.head()


# %%
# Standardize Class Day(s)

def extract_codes(str):
    return re.findall(r'\(([A-Z]+)\)', str)

df['Class Day(s)'] = df['Class Day(s)'].apply(extract_codes)
df = df.explode('Class Day(s)').reset_index(drop=True)
df.head()


# %%
# Export generic_finals_schedule.csv

# df.to_csv('../data/generic_finals_schedule.csv')

# %%
# Import input.csv

try:
    student_df = pd.read_csv('../data/input.csv')
    
except FileNotFoundError as e:
    print(e)
    print('Using sample data instead')
    student_df = pd.read_csv('../data/sample_input.csv')

student_df.head()

# %%
# Calculate finals schedule (output)

final_schedule_df = student_df.merge(right=df)
final_schedule_df.drop(['Class Time','Class Day(s)'], axis='columns', inplace=True)
final_schedule_df

# %%
# Export output.csv

final_schedule_df.to_csv('../data/output.csv')


