import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


tips =pd.read_csv("Tips.csv")
# facet on the columns with another variable
# facet on the columns and rows, set name of axes
sns.lmplot(x='total_bill', y='tip', data=tips, col='smoker',row='time').set_axis_labels('Total bill (in $ )', ' Tip ( in $ )')