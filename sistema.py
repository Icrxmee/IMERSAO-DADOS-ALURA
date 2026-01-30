import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv") 

df.head()

df.info()

df.describe()

plt.figure(figsize= (8,5))
sns.barplot(data= df, x = 'experience_level', y = 'salary_in_usd')
plt.title('Salário Médio Por Senioridade')
plt.xlabel("Senioridade")
plt.ylabel("Salario Médio Anual (USD)")
plt.show()