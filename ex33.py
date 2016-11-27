# -- coding: utf-8 --


i = 0;
numbers = []

while i < 6:
	print ("At the top i is %d" % i)
	numbers.append(i)
	i = i+1
	print ("Number now: ", numbers)
	print ("At the buttom i is %d" % i)
	pass

print ("The numbers: ")

for num in numbers:
	print(num)
