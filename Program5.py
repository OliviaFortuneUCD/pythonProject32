import numpy as np
import pandas as pd
import seaborn as sns

tips =pd.read_csv("Tips.csv")
ax = sns.stripplot(x="smoker", y="total_bill", hue="day", data=tips)