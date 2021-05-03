import numpy as np
import pandas as pd
import seaborn as sns

tips =pd.read_csv("Tips.csv")
ax = sns.stripplot(x="total_bill", y="day", data=tips)