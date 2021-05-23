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
		row = int(loadjson[key]['numDataRows'])	
		#print(row)
		
		# [ all table cells column wise]
		
		#data = str(key+"\t")
		data = ""
		
		for i in range(col):
			for j in range(row):
				ij = loadjson[key]['data'][j][i]
				#print(loadjson[key]['data'][j][i])
				jj = ij.replace("\n"," ")
				jj = jj.replace("\t"," ")
				jj = jj.replace(" ","_")
				data = data + str(jj) + " "
		
		
		data = str(key+"\t")+data	
		fw.write(data+"\n")
		#print(data)
		#break	
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
		#break
	

fw.close()

