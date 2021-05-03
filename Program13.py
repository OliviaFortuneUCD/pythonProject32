import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


tips =pd.read_csv("Tips.csv")
sns.lmplot(x='total_bill',y='tip',data=tips,col='day',hue='gender',palette='coolwarm',
          aspect=0.6,size=8)