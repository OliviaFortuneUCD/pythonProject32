import numpy as np
import pandas as pd
import seaborn as sns

tips =pd.read_csv("Tips.csv")

g = sns.catplot(x="gender", y="total_bill",
                hue="smoker", col="time",
                data=tips, kind="strip",
                height=4, aspect=.7);