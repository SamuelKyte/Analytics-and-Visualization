'''

'''
 #  import package
import pandas as pd
df = pd.read_csv('balance.txt',sep=' ') #  read file
print(df.head()) # print first 5 rows (reference)


 #  Compare the average income based on ethnicity.
eth_grp = df.groupby(['Ethnicity']) #  create df filter
asian = eth_grp.get_group('Asian') #  filter for each ethnicity
afam = eth_grp.get_group('African American')
cauca = eth_grp.get_group('Caucasian')

 #  print mean for each df filter
print(f"\nAverage income for persons of Asian ethnicity is: R{asian['Income'].mean()}.")
print(f"Average income for persons of African American ethnicity is: R{afam['Income'].mean()}.")
print(f"Average income for persons of Caucasian ethnicity is: R{cauca['Income'].mean()}.\n")

 #  On average, do married or single people have a higher balance?
 #  repeat first challenge but with married and balance columns
married_grp = df.groupby(['Married'])
married = married_grp.get_group('Yes')
single = married_grp.get_group('No')

 #  print means
print(f"\nAverage debt balance for married people is: R{married['Balance'].mean()}.")
print(f"\nAverage debt balance for single people is: R{single['Balance'].mean()}.\n")

 #  What is the highest income in our dataset?
 #  sort df values and print highest
print(df.sort_values(by='Income',ascending=False).head(1))
print("\n")

 #  What is the lowest income in our dataset?
 #  sort df values and print lowest
print(df.sort_values(by='Income',ascending=True).head(1))
print("\n")

 #  How many cards do we have recorded in our dataset?
 #  Simple sum method for cards column
print(f'\nThere are {sum(df.Cards)} cards in our dataset.')


 #  How many females do we have information for vs how many males?
 #  just use pd value counts method for gender column
 #  counts entry for each subset in column
print(f"\nIn our dataset, we have information on: \n {pd.value_counts(df['Gender'])}")