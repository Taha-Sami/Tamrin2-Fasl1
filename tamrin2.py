import matplotlib.pyplot as plt
import numpy as np
### Part1
f=open("project_data.csv",'r')
t=f.read()
f.close()
lines=t.split('\n')
lines.pop(0)
lines.pop(-1)
l=[]
values_close=[]
day=[]
for i in range(0,len(lines)):
	a=lines[i].split(',')
	l.append(a)

for d in range(len(l)):
	values_close.append(l[d][5])
	day.append(l[d][1])

day.reverse()
values_close.reverse()

day=np.array(day)
values_close=np.array(values_close)

day = [int(n) for n in day]
values_close = [float(b) for b in values_close]



plt.plot(day,values_close,label='fameli chart')
plt.legend()
plt.xlabel('day')
plt.ylabel('price')
plt.show()

###plot gheymat
### Part2

dy=[]
for i in range(0,len(values_close)-1):
	f=0
	f=values_close[i+1]-values_close[i]
	dy.append(f) 


plt.plot(day[:-1],dy)
plt.xlabel('day')
plt.ylabel('price')
plt.show()

###plot moshtagh

###Part3
s=[]
for i in range(0,3397):
	group=[]
	group=values_close[i:i+10]
	s.append(group)

#print(s)                     ### dastebandi 10taii

m=[]
for i in range(0,3396):
	if s[i][9]>s[i+1][0]:
		m.append('True')
	else:
		m.append('False')

#print(m)                       ### True false