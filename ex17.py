# -- coding: utf-8 --

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print ("Copying from %s to %s" %(from_file, to_file))

input_file = open(from_file)
indata = input_file.read()

print ("The input file is %d byte long" %len(indata))

print ("Does the output file exist? %r" %exists(to_file))

print ("Ready, hit ENTER to continue, CTRL-C to abort.")

input("?")

output = open(to_file, 'w')

output.write(indata)

print ("Alright, all done")

output.close()

input_file.close()



