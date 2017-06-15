import pandas as pd

df = pd.read_json('https://raw.githubusercontent.com/onaio/ona-tech/master/data/water_points.json')
df = df[['water_functioning', 'communities_villages']]
df = df[df['water_functioning'] == 'yes'].groupby(['communities_villages']).count()
df['ranking'] = df['water_functioning'].rank(ascending=False)
df.to_json(orient='index')

total_functional = df['water_functioning'].sum()

#http://www.shanelynn.ie/summarising-aggregation-and-grouping-data-in-python-pandas/