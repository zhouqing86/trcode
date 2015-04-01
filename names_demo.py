import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
 
 
if __name__ == '__main__': 
    names1880 = pd.read_csv('data/names/yob1880.txt', names=['name', 'sex', 'births']) 
    print(names1880) 
 
    print('Use the sum of the births column by sex as the total number of births in that year:') 
    print(names1880.groupby('sex').births.sum()) 
 
    print('''Since the data set is split into files by year, one of the first things to do is to assemble 
all of the data into a single DataFrame and further to add a year field. This is easy to 
do using pandas.concat: 
    ''') 
    # 2013 is the last available year right now 
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
    print('All the names:') 
    print(names) 
 
    total_births = names.pivot_table('births', index='year', columns='sex', aggfunc=sum) 
    print(total_births) 
    total_births.plot(title='Total births by sex and year') 
 
    print('Insert a column prop with the fraction of babies given each name relative to the total number of births.') 
    def add_prop(group): 
        # Integer division floors 
        births = group.births.astype(float) 
        group['prop'] = births / births.sum() 
        return group 
    names = names.groupby(['year', 'sex']).apply(add_prop) 
    print(names) 
    # Verify that the prop column sums to 1 within all the groups. 
    print(np.allclose(names.groupby(['year', 'sex']).prop.sum(), 1)) 
 
    print('Extract a subset of the data to facilitate further analysis: the top 1000 names for each sex/year combination.') 
    def get_top1000(group): 
        return group.sort_index(by='births', ascending=False)[:1000] 
    grouped = names.groupby(['year', 'sex']) 
    top1000 = grouped.apply(get_top1000) 
    print(top1000) 
    boys = top1000[top1000.sex == 'M'] 
    girls = top1000[top1000.sex == 'F'] 
    total_births = top1000.pivot_table('births', index='year', columns='name', aggfunc=sum) 
    print('total_births:') 
    print(total_births) 
    subset = total_births[['John', 'Harry', 'Mary', 'Marilyn']] 
    print(type(subset)) 
    subset.plot(subplots=True, figsize=(12, 10), grid=False, title="Number of births per year") 
 
    print('Proportion of births represented by the top 1000 most popular names:') 
    table = top1000.pivot_table('prop', index='year', columns='sex', aggfunc=sum) 
    table.plot(title='Sum of table1000.prop by year and sex', yticks=np.linspace(0, 1.2, 13), xticks=range(1880, 2020, 10)) 
 
    print('We want to know how many of the most popular names it takes to reach 50%.') 
    def get_quantile_count(group, q=0.5): 
        group = group.sort_index(by='prop', ascending=False) 
        return np.searchsorted(group.prop.cumsum().values, q) + 1 
    diversity = top1000.groupby(['year', 'sex']).apply(get_quantile_count) 
    diversity = diversity.unstack('sex') 
    diversity.plot(title='Number of popular names in top 50%') 
    plt.show()