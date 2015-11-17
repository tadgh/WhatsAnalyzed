import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def author_counts(df):
    plt.figure()
    grouped = df.groupby('AUTHOR').count()
    grouped['TIME'].plot(kind='bar')
    plt.show()
