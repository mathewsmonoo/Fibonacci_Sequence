#Normal Fibonacci
def fibo(x):
	if ((x == 0) or (x == 1)):
		return 1
	else:
		return fibo(x - 1) + fibo(x - 2)

#Efficient Fibonacci (uses dict)
def fibo_eff(y,dict1):
	if y in dict1:
		return dict1[y]
	else:
		ans = fibo_eff(y-1,dict1) + fibo_eff(y-2,dict1)
		dict1[y] = ans
		return ans

dict1 = {1:1,2:2}

choice = 20 # Change here for different values

print('   | For {} |'.format(choice))
print('Fibo:\t\t',fibo(choice))
print('Efficient Fibo: ',fibo_eff(choice,dict1))