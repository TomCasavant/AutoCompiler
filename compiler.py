'''
	Filename: compiler.py
	Author: Tom Casavant
	Date Created: 1/28/2019
	Date Last Modified: 1/28/2019
'''
from os import listdir, system
from os.path import isfile, join
import sys


"""Compiles all files in a given directory using 'g++' compiler.
Usage: python compiler.py directory_name"""
if __name__ == "__main__":
	#Get folder
	if (len(sys.argv) > 1):
		folder = sys.argv[1]
	else:
		folder = raw_input("Enter the name of the directory: ")

	#Collects all files from directory
	files = [f for f in listdir(folder) if isfile(join(folder + "/", f))]

	#Compile all files
	for file in files:
		print("{} is compiling...".format(file))
		system("g++ {}/{}".format(folder, file))

	print("Finished compiling programs in {}".format(folder))
