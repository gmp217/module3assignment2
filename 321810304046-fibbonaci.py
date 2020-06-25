n=int(input('Enter no of terms: '))
n1,n2=0,1
if(n<0):
	print('Enter positive number')
elif(n==1):
	print(n1)
else:
	for i in range(0,n):
		print(n1)
		n=n1+n2
		n1=n2
		n2=n
