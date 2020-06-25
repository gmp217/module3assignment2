s=input('Enter a string: ')
m={}
for i in s:
	if i in m:
		m[i]+=1
	else:
		m[i]=1
print('Frequency of characters:',m)