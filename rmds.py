#! /usr/bin/env python

import argparse
import os

parser = argparse.ArgumentParser('rmds', description = "Recursively removes pesky .DS_Store files")

parser.add_argument("-s", action='store_true', help = "Process single directory; i.e. no recursion")
parser.add_argument("-d", "--DIRECTORY", default = './', help = "directory to remove files from")
parser.add_argument('-n', "--FILENAMES", nargs = "+", help = "filename(s) to remove, defaults to .DS_Store and ._.DS_Store",
					default = ['.DS_Store'])

args = parser.parse_args()

def remove_ds_files(actuallyDelete, directory, files):
	for filename in args.FILENAMES:
		if filename in files:
			if actuallyDelete:
				os.remove(os.path.join(directory,filename))
			else:
				print(os.path.join(directory,filename))
				
if __name__ == "__main__":
	if args.s == False:
		print("Continuing will delete these files:")
		os.path.walk(args.DIRECTORY, remove_ds_files, False)
		if raw_input('Proceed to delete files? y/N : ').lower() == 'y':
			os.path.walk(args.DIRECTORY, remove_ds_files, True)
	else:
		print("Continuing will delete these files:")
		remove_ds_files(False, args.DIRECTORY, os.listdir(args.DIRECTORY))
		if raw_input('Proceed to delete files? y/N : ').lower() == 'y':
			remove_ds_files(True, args.DIRECTORY, os.listdir(args.DIRECTORY))
