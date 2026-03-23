import pandas as pd

df = pd.read_csv('books.csv')

print(df)

author = input()
print(df[df['author'] == author])

publisher = input()
print(df[df['publisher'] == publisher])

cheap = df[df['price'] == df['price'].min()]
costly = df[df['price'] == df['price'].max()]
print(cheap['title'])
print(costly['title'])

print(df.sort_values(by='year'))