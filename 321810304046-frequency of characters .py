from collections import OrderedDict
def remove_duplicate(str1):
  return "".join(OrderedDict.fromkeys(str1))

s=input("enter i/p:")  
w=remove_duplicate(s)
print('Frequency of characters:')	
for i in w:
	print(i,s.count(i))
	
b,c="0123456789",0
for i in s:
 for j in b:
 	if(i==j):
 		c+=1
c=len(s)-c
print("total no of character in an enter string :",c)
