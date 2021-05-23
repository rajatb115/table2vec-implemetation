#Import required libraries

import os
import sys
import pandas as pd
from sklearn.model_selection import train_test_split


def split_fun(input_file_location, output_file_location,file_name, split_filename):
	#dir_path = '/scratch/cse/phd/anz208486/col873_project/NLP_project/Dataset'
	#if len(sys.argv)>1:
	#    filen = sys.argv[1]
	#else:
	#    filen = 'table2VecH.csv'
	dir_path = input_file_location
	filename = os.path.join(dir_path, file_name)
	df = pd.read_csv(filename, sep='\t', header=None)
	#print(df)
	df_train, df_test = train_test_split(df,test_size=0.3,random_state=27)
	#print('train:')
	#print(df_train.head())
	#print('test:')
	#print(df_test.head())
	filen = split_filename
	train_file = os.path.join(output_file_location,'train_'+filen)
	test_file = os.path.join(output_file_location,'test_'+filen)
	df_train.to_csv(train_file,sep='\t', index=False, header=False)
	df_test.to_csv(test_file,sep='\t', index=False, header=False)
	
	return(train_file,test_file)
