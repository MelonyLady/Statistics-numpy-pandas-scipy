import scipy.stats as stats
import pandas as pd
import numpy as np


# *** Psych Services***
ar = np.array([[89, 156], [426637, 803416]])
df = pd.DataFrame(ar, columns=["ps", "no_ps"])
df.index = ["A", "NT"]
print(df)

print()

df2 = df.copy()
df2.loc['Column_Total'] = df2.sum(numeric_only=True, axis=0)
df2.loc[:, 'Row_Total'] = df2.sum(numeric_only=True, axis=1)
print(df2)

print()

oddsratio, pvalue = stats.fisher_exact([[89, 156], [426637, 803416]])
print(f'pvalue= {pvalue}')
print(f'oddsratio = {oddsratio}')


print()
print("*****************************************************************************")
print()

# *** Ventilation non-invasive

ar = np.array([[96, 149], [610667, 619386]])
df = pd.DataFrame(ar, columns=["ventnoninv", "no_ventnoninv"])
df.index = ["A", "NT"]
print(df)

print()

df2 = df.copy()
df2.loc['Column_Total'] = df2.sum(numeric_only=True, axis=0)
df2.loc[:, 'Row_Total'] = df2.sum(numeric_only=True, axis=1)
print(df2)

print()

oddsratio, pvalue = stats.fisher_exact([[96, 149], [610667, 619386]])
print(f'pvalue= {pvalue}')
print(f'oddsratio = {oddsratio}')


print()
print("*****************************************************************************")
print()

