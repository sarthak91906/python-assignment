import pandas as pd

data = {
    'State': ['Maharashtra', 'Gujarat', 'Rajasthan', 'Karnataka', 'Tamil Nadu'],
    'Area': [307713, 196244, 342239, 191791, 130058],
    'Population': [112374333, 60439692, 68548437, 61095297, 72147030]
}

df = pd.DataFrame(data)

print(df)

print(df.loc[df['Area'].idxmax(), 'State'])

print(df.loc[df['Population'].idxmax(), 'State'])

df['Density'] = df['Population'] / df['Area']

print(df)

print(df.loc[df['Density'].idxmax(), 'State'])

print(df.loc[df['Population'].idxmin(), 'State'])