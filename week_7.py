
import pandas as pd
import matplotlib.pyplot as plt

pd.options.display.max_rows = 999

df = pd.read_csv('data.csv')

#reading the first 10 rows
print(df.head(10))

#Mean of calories

df['Calories'].mean()

#Mode of Pulse

df['Pulse'].mode()[0]

#Median for calories

df['Calories'].median()



#Histograph

df['Duration'].plot(kind='hist')

#Removing empty cells
df.dropna(inplace=True)

#Plotting scatter plot
df.plot(x='Duration',y='Calories',kind='scatter')
plt.show()
