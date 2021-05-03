import numpy as np
import pandas as pd
import seaborn as sns



tips =pd.read_csv("Tips.csv")

ax = sns.boxplot(x="day", y="total_bill", data=tips)
