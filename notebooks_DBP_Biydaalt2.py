import pandas as pd
import numpy as np
import os 
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
os.chdir(r"C:\Users\USER\Downloads\Бие даалт - 2.xlsx")
c1=pd.read_excel('Бие даалт - 2.xlsx', sheet_name='Нийт')
import matplotlib.pyplot as plt
import numpy as np
# 1
a1=pd.read_excel('Бие даалт - 2.xlsx', sheet_name='Оюутнуудын нэмэлт мэдээлэл')
list1=a1['Оюутны код'].tolist()
def second_let(x):
    lst= []
    for wrd in x:
        lst.append(int(wrd[2]))
    return lst
second_let(list1)
ser1=pd.Series(second_let(list1))
ser2=12-ser1
a1['Unnamed: 8']=pd.Series.replace(ser2)
a1= a1.rename(columns={'Unnamed: 8': 'Курс'})
a1
# 2
x1=pd.read_excel('Бие Даалт - 2.xlsx', sheet_name='Ирц')
y1=pd.read_excel('Бие Даалт - 2.xlsx', sheet_name='Шалгалт')
x = np.array(x1["Нийт -10"]).reshape((-1, 1))
y = np.array(y1["Нийт"])
reg = LinearRegression().fit(x, y)
r_sq = reg.score(x, y)
print(r_sq)
print('intercept:', reg.intercept_)
print('slope:', reg.coef_)
# 3
x3=np.array(a1['Судалсан хичээлийн тоо']).reshape((-1, 1))
y3=np.array(a1['Голч дүн'])
reg3=LinearRegression().fit(x3, y3)
print('intercept:', reg3.intercept_)
print('slope:', reg3.coef_)
# 4
x2=np.array(a1['ЭЕШ оноо']).reshape((-1, 1))
y2=np.array(a1['Голч дүн'])
reg2=LinearRegression().fit(x2, y2)
print('intercept:', reg2.intercept_)
print('slope:', reg2.coef_)
# 4
x2=np.array(a1['ЭЕШ оноо'])
y2=np.array(a1['Голч дүн'])
plt.plot(x2, y2,'o')
b1, b0 = np.polyfit(x2, y2,1)
plt.plot(x2, b1*x2 + b0)
# 5
eysh_golch= reg2.intercept_+reg2.coef_*620
eysh_golch
# 6
c2=c1['Нийт'].drop(28,axis=0)
c2
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
langs=a1['Оюутны нэр'].tolist()
percents=c2.tolist()
ax.bar(langs,percents)
plt.title('Дүнгүүд-bar chart')
plt.show()
# 7
x= a1['Оюутны нэр'].tolist()
y= c2.tolist()
plt.title('Дүнгүүд-line chart')
plt.plot(x,y) 
plt.show() 
# 8
g1=0
g2=0
g3=0
g4=0
g5=0
for i in y:
    if i>90:
        g1+=1
    elif 90>i and i>80:
        g2+=1
    elif 80>i and i>70:
        g3+=1 
    elif 70>i and i>60:
        g4+=1
    else:
        g5+=1
fig2 = plt.figure()
ax2 = fig2.add_axes([0,0,1,1])
ax2.axis('equal')
langs2 =['A','B','C','D','F']
percents2=[g1,g2,g3,g4,g5]
ax2.pie(percents2, labels = langs2,autopct='%1.2f%%')
plt.title('Дүнгүүд-pie chart')
plt.show()
# 9
f1=0
f2=0
f3=0
f4=0
f5=0
f6=0
f7=0
f8=0
f9=0
for i in a1['Суралцаж буй мэргэжил']:
    if i=='НББ':
        f1+=1
    elif i=='ЭЗО':
        f2+=1
    elif i=='СУ':
        f3+=1 
    elif i=='АЯЛАЛ ЖУУЛЧЛАЛ':
        f4+=1
    elif i=='БАНК':
        f5+=1
    elif i=='МКТ':
        f6+=1
    elif i=='МСМ':
        f7+=1
    elif i=='ЭРХ ЗҮЙ':
        f8+=1
    else:
        f9+=1
fig3 = plt.figure()
ax3 = fig3.add_axes([0,0,1,1])
ax3.axis('equal')
langs3 = ['НББ','ЭЗО','СУ','АЯЛАЛ ЖУУЛЧЛАЛ','БАНК','МКТ','МСМ','ЭРХ ЗҮЙ','БУ']
percents3 = [f1,f2,f3,f4,f5,f6,f7,f8,f9]
ax3.pie(percents3, labels = langs3,autopct='%1.2f%%')
plt.title('Тэнхимүүд- Pie chart')
plt.show()
# 9
fig3 = plt.figure()
ax3 = fig3.add_axes([0,0,1,1])
langs3 = ['НББ','ЭЗО','СУ','АЯЛАЛ ЖУУЛЧЛАЛ','БАНК','МКТ','МСМ','ЭРХ ЗҮЙ','БУ']
percents3 = [f1,f2,f3,f4,f5,f6,f7,f8,f9]
ax3.bar(langs3,percents3,color=['blue', 'red', 'green', 'blue', 'cyan','purple','pink','blue','red'])
plt.title('Тэнхимүүд- Bar chart')
plt.show()
# 10
eysh2=np.array(a1['ЭЕШ оноо'])
golch2=np.array(a1['Голч дүн'])
pearson_corr = np.corrcoef(eysh2, golch2)
pearson_corr