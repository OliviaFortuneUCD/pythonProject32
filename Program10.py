import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


tips = sns.load_dataset("tips")
# facet on the columns with another variable
sns.relplot(x='total_bill', y='tip', hue='day', col='time', data = tips)