import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('company_sales_data.csv')

plt.figure()
plt.plot(df['month_number'], df['total_profit'])
plt.xlabel('Month')
plt.ylabel('Total Profit')
plt.title('Total Profit Per Month')
plt.show()

plt.figure()
products = ['facecream','facewash','toothpaste','bathingsoap','shampoo','moisturizer']
for p in products:
    plt.plot(df['month_number'], df[p], label=p)
plt.xlabel('Month')
plt.ylabel('Sales')
plt.legend()
plt.title('Sales Data of Products')
plt.show()

plt.figure()
plt.bar(df['month_number'], df['facecream'], label='Face Cream')
plt.bar(df['month_number'], df['facewash'], bottom=df['facecream'], label='Face Wash')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.legend()
plt.title('Face Cream and Face Wash Sales')
plt.show()

totals = [df[p].sum() for p in products]
plt.figure()
plt.pie(totals, labels=products, autopct='%1.1f%%')
plt.title('Total Sales Distribution')
plt.show()