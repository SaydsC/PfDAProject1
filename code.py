#Project Code
# Author: Sadie Concannon

#Requisite libraries and setings for analysis
#Imported libraries:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt #for plotting
import sys
import seaborn as sns

attrition = pd.read_csv("HR-Employee-Attrition.csv")

# attrition.head() #tells us the data has 22 columns and 1000 rows we can print the dataset 
# to determine what variables we want to work with i.e. column headings

#print(attrition.head(20))
#Once imported I was able to to use various commmands to draw whole data from the data set or specific data as 
# specified in the column title in the csv file e.g. using commands such as; attrition.describe() to get statistical insight 
# like the count, mean values, standard deviation 
# attrition.info() to print information about the dataset including the index dtype and columns, non-null values and memory usage.

#attrition.describe()
#attrition.info()

def summary_to_file():
    sys.stdout = open("summary.txt","w")
    print ("\n")
    sys.stdout.close()


#start with a simple histogram amended to have 4 on one page
fig, axes = plt.subplots(2, 2, figsize=(10,10))

axes[0,0].set_title("Attrition")
axes[0,0].hist(attrition['Attrition'], bins=10)

axes[0,1].set_title("Age")
axes[0,1].hist(attrition['Age'], bins=10) 

axes[1,0].set_title("Gender")
axes[1,0].hist(attrition['Gender'], bins=10)

axes[1,1].set_title("Years Service")
axes[1,1].hist(attrition['YearsAtCompany'], bins=10)
#plt.show()

#scatterplot
f = plt.figure(figsize=(6,3))
fig = sns.scatterplot(x="YearsAtCompany", y="Attrition", data=attrition)

sns.set()
#plt.show()

#swarmplot
f=plt.figure(figsize=(20,13))
sns.swarmplot(x="Attrition", y="YearsAtCompany", hue="Gender", data=attrition)
#plt.show()

#stripplot
f=plt.figure(figsize=(10, 6))
sns.stripplot(x="Attrition", y="Position", hue="Gender", data=attrition)
#plt.show()

#pairplot
f=plt.figure(figsize=(25,13))
sns.pairplot(data=attrition, vars=["Gender", "Attrition", "YearsAtCompany", "JobLevel"])
plt.show()