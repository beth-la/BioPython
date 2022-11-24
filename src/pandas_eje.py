import pandas as pd 
import matplotlib.pyplot as plt

ecoli = pd.Series([1,2,3,4,5], name = "matraz", index =[1,2,3,4,5])
#print(ecoli.values)
prot_genes = pd.read_csv('data/prot_genes.csv',index_col='Organism', squeeze=True)

organism = pd.read_csv('docs/Organism.csv', squeeze=True)


ax = organism.value_counts().plot.bar()
fig = ax.get_figure()
fig.savefig('figure.pdf')
