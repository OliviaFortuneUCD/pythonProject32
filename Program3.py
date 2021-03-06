import numpy as np
import pandas as pd
import seaborn as sns
from scipy.stats import pearsonr

tips =pd.read_csv("Tips.csv")
ax = sns.stripplot(x="day", y="total_bill", data=tips, jitter=0.05)


list1 = tips['tips']
list2 = tips['total_bill']


# Apply the pearsonr()
corr, _ = pearsonr(list1, list2)
print('Pearsons correlation: %.3f' % corr)
