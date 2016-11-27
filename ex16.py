# -- coding: utf-8 --

from sys import argv

script, filename = argv

print ("We're going to erase %r." %filename)

print ("If you don't want that, hit CTRL-C (^C).")

print ("If you do want that, hit ENTURE.")

input ("?")


print ("Opening the file...")

target = open(filename, 'a+')

#print (target.read())

print ("Truncating the file. Goodby!")

target.truncate()

print ("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print ("I am going to write these to the file.")

target.write(line1)
target.write("\n")

target.write(line2)
target.write("\n")

target.write(line3)
target.write("\n")

print ("Add finally, we close it.")

target.close()

target_again = open(filename)

print (target_again.read())

target_again.close()


