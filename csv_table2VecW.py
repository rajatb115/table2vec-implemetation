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
		
		# [page_title, section title, table caption, table headings, and all table cells ]
		
		#data = str(key+"\t")
		data = ""
		
		pgTitle = str(loadjson[key]['pgTitle'])
		pgTitle = pgTitle.replace("\n"," ")
		pgTitle = pgTitle.replace("\t"," ")
		pgTitle = pgTitle.replace(" ","_")
		
		data = data + pgTitle+ " "

		secondTitle = str(loadjson[key]['secondTitle'])
		secondTitle = secondTitle.replace("\n"," ")
		secondTitle = secondTitle.replace("\t"," ")
		secondTitle = secondTitle.replace(" ","_")
		
		data = data + secondTitle + " "

		caption = str(loadjson[key]['caption'])
		caption = caption.replace("\n"," ")
		caption = caption.replace("\t"," ")
		caption = caption.replace(" ","_")
		
		data = data + caption + " "
		
		str_csv = loadjson[key]['title']
		
		for i in str_csv:
			j = i.replace("\n"," ")
			j = j.replace("\t"," ")
			j = j.replace(" ","_")
			data = data + str(j) + " "
		
		row = int(loadjson[key]['numDataRows'])
		row_data = loadjson[key]['data']
		for r_data in row_data:
			for c_data in r_data:
				j = c_data.replace("\n"," ")
				j = j.replace("\t"," ")
				j = j.replace(" ","_")
				data = data + str(j) + " "	
		
		#if ( data.find("\n")> -1 ):
		#	print("present \\n")
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

