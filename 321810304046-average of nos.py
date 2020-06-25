n=int(input('Enter no of integers: '))
m=0
print('Enter values:')
for i in range(0,n):
	i=int(input())
	m=m+i
print('Average: ',m/n)