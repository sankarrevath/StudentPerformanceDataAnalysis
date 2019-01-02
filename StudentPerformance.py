import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

passmark = eval(input("Enter the passing mark: "))

input_str = input('Select a Label to Ananlyze: "parental level of educaion","gender","race/ethnicity","lunch","test preparation course"')

df = pd.read_csv('StudentsPerformance.csv')

print(df.shape) #prints shape (1000,8)

print(df.describe())

#explore the math score across all labels
p = sns.countplot(x='math score', data = df, palette='muted')
_ = plt.setp(p.get_xticklabels(), rotation = 90)

plt.show()

df['Math_PassStatus'] = np.where(df['math score']<passmark, 'F','P')
print(df.Math_PassStatus.value_counts()) #P and F count @45 passmark   P:924 F:76

p = sns.countplot(x=input_str, data = df, hue='Math_PassStatus', palette='bright')
_ = plt.setp(p.get_xticklabels(), rotation = 90)
plt.show()


################################################################################
#lets explore the reading scores

sns.countplot(x='reading score', data=df, palette='muted')
plt.show()

df['Reading_PassStatus'] = np.where(df['reading score']<passmark, 'F','P')
print(df.Reading_PassStatus.value_counts()) #P and F count @45 passmark P:947  F:53

p = sns.countplot(x= input_str, data=df, hue='Reading_PassStatus',palette='bright')
_ = plt.setp(p.get_xticklabels(), rotation = 90)

#################################################################################
#exploring the writing score

p = sns.countplot(x='writing score', data = df, palette='muted')
_ = plt.setp(p.get_xticklabels(), rotation = 90)

df['Writing_PassStatus'] = np.where(df['writing score']<passmark, 'F', 'P')
print(df.Writing_PassStatus.value_counts())# P and F count @45 passmark P:930 F:70

p = sns.countplot(x = input_str, data = df, hue = 'Writing_PassStatus', palette='bright')
plt.setp(p.get_xticklabels(), rotation = 90)
plt.show()

##################################################################################
#overall score

df['Overall_PassStatus'] = df.apply(lambda x: 'F' if x['Math_PassStatus'] == 'F' or x['Reading_PassStatus'] == 'F' or x['Writing_PassStatus'] == 'F' else 'P', axis = 1)
df.Overall_PassStatus.value_counts()#P and F count @ passmark 45 P:949 F:51


p = sns.countplot(x = input_str, data = df, hue = 'Overall_PassStatus', palette='bright')
_ = plt.setp(p.get_xticklabels(), rotation = 90)
plt.show()

df['Total_Marks'] = df['math score'] + df['reading score'] + df['writing score']
df['Percentage'] = df['Total_Marks']/3

p = sns.countplot(x = 'Percentage', data = df, palette='muted')
_ = plt.setp(p.get_xticklabels(), rotation = 0)
plt.show()


###########################################################################
#label distribution with grades

def getGrade(Percentage, Overall_PassStatus):
    if(Overall_PassStatus == 'F'):
        return 'F'
    if(Percentage >= 90):
        return 'A'
    if(Percentage >= 80):
        return 'B'
    if(Percentage >= 70):
        return 'C'
    if(Percentage >= 60):
        return 'D'
    else:
        return 'F'

df['Grade'] = df.apply(lambda x: getGrade(x['Percentage'], x['Overall_PassStatus']), axis = 1)
print(df.Grade.value_counts())

sns.countplot(x='Grade', data=df, order=['A','B','C','D','F'], palette='muted')
plt.show()

p = sns.countplot(x = input_str, data = df, hue='Grade', palette='bright')
_ = plt.setp(p.get_xticklabels(), rotation= 90)



















