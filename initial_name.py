import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

years = range(1880, 2014) 
pieces = [] 
columns = ['name', 'sex', 'births'] 
for year in years: 
    path = 'data/names/yob%d.txt' % year 
    frame = pd.read_csv(path, names=columns) 
    frame['year'] = year 
    pieces.append(frame) 
# Concatenate everything into a single DataFrame 
names = pd.concat(pieces, ignore_index=True) 

def add_prop(group): 
        # Integer division floors 
        births = group.births.astype(float) 
        group['prop'] = births / births.sum() 
        return group 
names = names.groupby(['year', 'sex']).apply(add_prop) 

pieces = []
for year, group in names.groupby(['year', 'sex']):
	pieces.append(group.sort_index(by='births', ascending=False)[:1000])
top1000 = pd.concat(pieces, ignore_index=True)


total_births = top1000.pivot_table('births',index="year",columns="name",aggfunc=sum)
subset = total_births[['John', 'Harry', 'Mary', 'Marilyn']]title="Number of births per year")

subset.plot(subplots=True, figsize=(12, 10), grid=False,title="Number of births per year")

table = top1000.pivot_table('prop', rows='year', cols='sex', aggfunc=sum)

boys = top1000[top1000.sex == 'M'] 
girls = top1000[top1000.sex == 'F']
df = boys[boys.year == 2010]
#we want to know how many of the most popular names it takes to reach 50% 
prop_cumsum = df.sort_index(by='prop', ascending=False).prop.cumsum()
prop_cumsum.searchsorted(0.5)

def get_quantile_count(group, q=0.5):
	group = group.sort_index(by='prop', ascending=False)
	return group.prop.cumsum().searchsorted(q)[0] + 1

get_last_letter = lambda x: x[-1]

table = names.pivot_table('births', rows=last_letters, cols=['sex', 'year'], aggfunc=sum)

get_last_letter = lambda x: x[-1]
last_letters = names.name.map(get_last_letter)
last_letters.name = 'last_letter'
table = names.pivot_table('births', rows=last_letters, cols=['sex', 'year'], aggfunc=sum)

subtable = table.reindex(columns=[1910, 1960, 2010], level='year')
subtable.head()
subtable.sum()

letter_prop = subtable / subtable.sum().astype(float)

import matplotlib.pyplot as plt
fig, axes = plt.subplots(2, 1, figsize=(10, 8))
letter_prop['M'].plot(kind='bar', rot=0, ax=axes[0], title='Male')
letter_prop['F'].plot(kind='bar', rot=0, ax=axes[1], title='Female',legend=False)

letter_prop.ix[['d', 'n', 'y'], 'M'].T
letter_prop = table / table.sum().astype(float)
dny_ts = letter_prop.ix[['d', 'n', 'y'], 'M'].T
dny_ts.plot()

all_names = top1000.name.unique()
mask = np.array(['lesl' in x.lower() for x in all_names])
lesley_like = all_names[mask]

filtered = top1000[top1000.name.isin(lesley_like)]
filtered.groupby('name').births.sum()



