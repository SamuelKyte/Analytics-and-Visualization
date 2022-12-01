 #  read data from a file into a pandas DataFrame.
import numpy as np
import pandas as pd

#Read data from the file called 'credit.csv' into a DataFrame
credit = pd.read_csv('credit.csv',
                            delim_whitespace = 1) #  specify that the delimiter is a single space
print(credit[:10]) #  print first 10 rows
print(credit.loc[:, ["Age","Education"]]) #  prints age and ed columns

rslts_credit = credit[credit['Age'] > 30] #  set condition for age
print(rslts_credit) #  print results