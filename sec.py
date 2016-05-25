num1 = input('Enter a number ')
num1 = int(num1)

num2 = input('Enter a number ')
num2 = int(num2)


try :
	num = num1/num2
	print('The result for num1/num2 is',num)
except BaseException as e:
	print('Exception:',e)
#finally:
#	print('End')
