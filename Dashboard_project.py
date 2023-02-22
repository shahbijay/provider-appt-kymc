# Import libraries

import pandas as pd
import seaborn as sns

import matplotlib
import matplotlib.pyplot as plt
plt.style.use('ggplot')
from matplotlib.pyplot import figure

%matplotlib inline
matplotlib.rcParams['figure.figsize'] = (12,8)  # Adjust the configuration of the plots we will create


# Read in the data

df = pd.read_csv('C:\Users\Bijay Shah\Downloads\movies.csv\movies.csv' 'r')