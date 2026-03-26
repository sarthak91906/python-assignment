import pandas as pd

df = pd.read_excel('employee.xlsx')

print(df[df['Department']=='Automotive'])

emp_id = int(input())
print(df[df['Employee ID']==emp_id])

print(df[df['Designation']=='Developer'])