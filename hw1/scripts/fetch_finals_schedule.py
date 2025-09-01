# %%
import requests

# %%
url = 'https://www.unr.edu/admissions/records/academic-calendar/finals-schedule'
response = requests.get(url=url)
with open(file='../html/output.html', mode='w') as f:
    f.write(response.text)


