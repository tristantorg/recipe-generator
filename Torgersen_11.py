"""
Assignment 11 Tristan Torgersen
"""

import json, re
with open('/Users/tristan/Downloads/yelp_AZ_2018.json', encoding='utf-8') as fin, open('/Users/tristan/Downloads/review_data.csv', mode='w') as fout:
    fout.write('Stars,N_feature1,N_feature2\n')  # open the in file and the outfile
    for review in fin:
        review = json.loads(review) # open as json file
        matches1 = re.findall(r'!+', review['text'], flags=re.I)  # regular expression to find exclamation points
        matches2 = re.findall(r'\b[A-Z]+\b', review['text'])  # regular expression to find all caps words
        num_matches1 = len(matches1)  # get number of instances for both linguistic features
        num_matches2 = len(matches2)
        fout.write(str(review['stars']) + ',' + str(num_matches1) + ',' + str(num_matches2) + '\n')  # write to the outfile 3 collumns with the number of stars, then the numbers of instances of the ling features

import pandas
yelp = pandas.read_csv('/Users/tristan/Downloads/review_data.csv', sep=',')

# calculating Pearson's correlation coefficient
from scipy.stats.stats import pearsonr
correlation1 = pearsonr(yelp.N_feature1, yelp.Stars)  # the format is: DataFrame.Column
correlation2 = pearsonr(yelp.N_feature2, yelp.Stars)
print(correlation1)
print(correlation2)

import matplotlib.pyplot as plt
import seaborn

# creating a scatterplot for exclamation points
seaborn.lmplot(x='N_feature1', y='Stars', data=yelp, fit_reg=True)  # 'x' is the x-axis, 'y' is the y-axis, and 'data' is the pandas DataFrame, and 'fit_reg' indicates whether a regression line should be drawn through the data points
plt.show()  # display the plot

# creating a scatterplot for all caps words
seaborn.lmplot(x='N_feature2', y='Stars', data=yelp, fit_reg=True)  # 'x' is the x-axis, 'y' is the y-axis, and 'data' is the pandas DataFrame, and 'fit_reg' indicates whether a regression line should be drawn through the data points
plt.show()  # display the plot
