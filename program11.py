import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


tips =pd.read_csv("Tips.csv")
# facet on the columns with another variable
sns.lmplot(x='total_bill', y='tip', data=tips, hue='smoker')