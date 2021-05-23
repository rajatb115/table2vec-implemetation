import json
import os
from os.path import isfile,join

def process_file(inputfile,fw):

	fr = open(inputfile,'r')
	
	readline = fr.read()
	#print(readline)
	loadjson = json.loads(readline)
	#print(loadjson)
	
	#get the level 1 keys of json (level 1 keys are table name)	
	keys = loadjson.keys()
	#print(keys)
	for key in keys:
		#print(key)
		#print(loadjson[key])
		col = int(loadjson[key]['numCols'])
		#print(col)
		#data = str(key+"\t")
		data =""
		str_csv = loadjson[key]['title']
		
		for i in str_csv:
			j = i.replace("\n"," ")
			j = j.replace("\t"," ")
			# j = j.replace(" ","_")
			data = data + j + " "
		
		#if ( data.find("\n")> -1 ):
		#	print("true")
		#	data = data.replace("\n"," ")
		#if (data.find("\t") > -1):
		#	print("present \\t")
		#	data = data.replace("\t"," ")
		
		data = str(key+"\t")+data		
		fw.write(data+"\n")
		#print(data)
			
	#close the open files
	fr.close()


# open the folder and read the files and folder in that folder
folder = input("Enter the folder loaction of the corpus : ")
file_list = os.listdir(folder)

outputfile = input("Enter the file name to write : ")
fw = open(outputfile,'w')

for files in file_list:
	# check if it is a file
	if isfile(join(folder,files)):	
		process_file(join(folder,files),fw)
		print(files," : is processed")
	

fw.close()

