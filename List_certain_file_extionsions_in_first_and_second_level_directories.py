#!/usr/bin/python
#2017-02-06 - Initial release
#Source: RENCKENS, M. & READSEARCH. (2017) List certain file extionsions in first and second level directories
# READSEARCH.be

#How to use this script?
#First, make sure Python 3.0 is installed on your device (https://www.python.org/)
#Then, open the commandprompt and change the directory to where all files are stored.
# An example on Windows: cd C:\Users\USERFOLDER\Documents/FOLDER_WITH_FILES
# An example on Ubuntu 14: cd/home/USERFOLDER/Documents/FOLDER_WITH_FILES
#At last, cal this script by first calling Python and then the location of the script
# An example on Windows with python 2: C:\Python27\python.exe C:\Users\famil\Desktop\Python\List_certain_file_extionsions_in_first_and_second_level_directories.py
# An example on Windows with python 3: py C:\Users\famil\Desktop\Python\List_certain_file_extionsions_in_first_and_second_level_directories.py
# An example on Ubuntu 14 with python 2: python List_certain_file_extionsions_in_first_and_second_level_directories.py
# An example on Ubuntu 14 with python 3: python3 List_certain_file_extionsions_in_first_and_second_level_directories.py

#-------------------------------------------------
import os, sys, re

#For which extension should be searched?
desiredExtension = '.TextGrid'
#Define header for the file
header = '# ' + sys.argv[0] + ' (Renckens, M. & READSEARCH, 2017)\nFirst and second level subdirectories are searched and files ending on ' + desiredExtension + ' are listed below.\n\n'
#Gather all output information
directoryList = "" + header
#Remember statistics
amountOfFiles = 0
amountOfSubFolders = 0
amountOfSkippedFiles = 0



#-------------------------------------------------
# Start
try:
	directories1 = sorted(os.listdir('.'))
except:
	print("Problem with inputting files.")


try:
	#first, process the extensions found in this directory
	for item1 in directories1:
		#do not process .DS_Store, invisible files or not desired file extensions
		if (os.path.isdir(item1) or item1.endswith((desiredExtension)) and not item1.startswith(('._')) ):
			directoryList+=item1 + "\n"
		else:
			amountOfSkippedFiles += 1

		#if item1 = a folder, process all first-level subdirectories
		if (os.path.isdir(item1) ):
			amountOfSubFolders+=1
			#get all filenames for each subdirectory again
			directories2 = sorted(os.listdir(os.path.join('.', item1)))
			for item2 in directories2:
				#do not process .DS_Store, invisible files or not desired file extensions
				if (os.path.isdir(os.path.join('.', item1, item2)) or item2.endswith((desiredExtension)) and not item2.startswith(('._')) ):
					directoryList+="\t" + item2 + "\n"
				else:
					amountOfSkippedFiles += 1

				#if item2 = a folder, process all second-level subdirectories
				if (os.path.isdir(os.path.join('.', item1, item2)) ):
					amountOfSubFolders+=1
					#get all filenames for each subdirectory again
					directories3 = sorted(os.listdir(os.path.join('.', item1, item2)))
					for item3 in directories3:
						#do not process .DS_Store, invisible files or not desired file extensions
						if (os.path.isdir(os.path.join('.', item1, item2, item3)) or item3.endswith((desiredExtension)) and not item3.startswith(('._')) ):
							directoryList+="\t\t" + item3 + "\n"
						else:
							amountOfSkippedFiles += 1
				


except Exception, e:
	print("File input problem: %s." % (e) )
	exit()


try:
	handle = open('list of files.txt','w')
	handle.write(directoryList)
	handle.close()
except:
	print('!!! Could not output text')



print("======================================================")
print("Processed %s subfolders in this directory" % (amountOfSubFolders) )
print("Skipped %s items:"  % (amountOfSkippedFiles))
print("    files named .DS_Store, filenames starting with ._")
print("    OR files with a different extension than required")
print("Job finished =========================================")

#--- EOF -----------------------------------------
