import pandas as pd

def calculate(url):
    """
        This function downloads and computes the aggregation of functional and non-functional water sources
        per community. The result is merged with the total number of functional water sources in all communities.
        A ranking is based on the percentage of faulty water sources per community.
    """
    df = pd.read_json(url)
    df = df[['water_functioning', 'communities_villages']]
    df = df.groupby(['communities_villages', 'water_functioning']).size().unstack()
    df = df.fillna(0)

    df['total'] = df['yes'] + df['no']
    df['fault_percentage'] = df['no'] / df['total']
    df['ranking'] = df['fault_percentage'].rank(ascending=False)

    total_functional = df['yes'].sum()
    df = df.rename(columns={'yes': 'functional', 'no':'non_functional'})
    df = df[['functional', 'non_functional', 'total', 'ranking']]
    records = df.to_json(orient='index')
    result = '{"number_functional": %s, %s}' % (total_functional, records)
    return result


print calculate('https://raw.githubusercontent.com/onaio/ona-tech/master/data/water_points.json')

