import numpy as np
import pandas as pd
import seaborn as sns

tips =pd.read_csv("Tips.csv")
ax = sns.violinplot(x="day", y="total_bill", data=tips,
                    inner=None, color=".8")
ax = sns.stripplot(x="day", y="total_bill", data=tips)