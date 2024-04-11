import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns

def plot_density(df, column_name):
    sns.set_theme(style="whitegrid")
    sns.kdeplot(data=df[column_name], shade=True)
    sns.despine(left=True, bottom=True)
    plt.xlabel(column_name)
    plt.ylabel('Density')
    plt.title('Density Plot of {}'.format(column_name))
    plt.show()

def plot_continuous_features(df, feature1, feature2):
    sns.set_theme(style="whitegrid")
    sns.lineplot(x=feature1, y=feature2, data=df)
    plt.xlabel(feature1)
    plt.ylabel(feature2)
    plt.title('{} vs {}'.format(feature1, feature2))
    plt.show()