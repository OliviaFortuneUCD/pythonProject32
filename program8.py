import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


tips =pd.read_csv("Tips.csv")
tips.hist();
