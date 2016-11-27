# -- coding: utf-8 -- 

#	python ex20.py test.txt
#
#	test.txt:
#	To all the people out there.
#	I say I don't like my hair.
#	I need to shave it off.



from sys import argv

script, input_file = argv

def print_all(f):
	print (f.read())

def rewind(f):
	f.seek(0)	#重新定位在文件的第0位及开始位置 

def print_a_line(line_count, f):
	print (line_count, f.readline())

current_file = open(input_file)

print ("First let's print the whole file:\n")

print_all(current_file)

print ("Now let's rewind, kind of like a tape.")

rewind (current_file)

print ("Let's print three lines:")

current_line = 1
print_a_line (current_line, current_file)

current_line = current_line + 1
print_a_line (current_line, current_file)

current_line = current_line + 1
print_a_line (current_line, current_file)



