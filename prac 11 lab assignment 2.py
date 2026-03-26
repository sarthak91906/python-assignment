import matplotlib.pyplot as plt

companies = ['Microsoft','Google','Amazon','IBM','Deloitte','Capgemini','Atos','Amdocs']
recruits = [120,150,180,90,110,130,95,100]

plt.figure()
plt.bar(companies, recruits)
plt.xticks(rotation=30)
plt.title('Recruitments by Company')
plt.show()

plt.figure()
plt.pie(recruits, labels=companies, autopct='%1.1f%%')
plt.title('Recruitment Share')
plt.show()

plt.figure()
explode = [0,0.1,0,0,0,0,0,0]
plt.pie(recruits, labels=companies, autopct='%1.1f%%', explode=explode)
plt.title('Customized Pie Chart')
plt.show()

plt.figure()
plt.pie(recruits, labels=companies, wedgeprops=dict(width=0.4), autopct='%1.1f%%')
plt.title('Doughnut Chart')
plt.show()

plt.figure()
labels = ['IBM','Amdocs']
values = [recruits[3], recruits[7]]
plt.bar(labels, values)
plt.title('IBM vs Amdocs Recruitment')
plt.show()