import pandas as pd
# data cleaning and columns selection

file = pd.read_csv("/Users/yahyaghrab/Downloads/Arabic Poem Comprehensive Dataset (APCD) 3.csv")
file.head()



file.columns[3]
file.columns[7]
new_data = file[[file.columns[7]], file.columns[3]]
new_data.head()
new_data.dropna(axis = 0, how= 'any', inplace = True)

new_data.to_csv("/Users/yahyaghrab/Downloads/Arabic Poem Comprehensive Dataset (APCD)_no_na.csv",index=False)
new_data.iloc[0]