# Importing the required libraries.
import numpy as np
#import pickle, zlib
from random import sample
import scipy.cluster.hierarchy as sch
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from sklearn.metrics.pairwise import cosine_similarity
from gensim import corpora
import pandas as pd
import pickle        
import gensim
import os
import csv
import sys
 
# dir_datasets = '/scratch/cse/phd/anz208486/col873_project/Datasets'     
# dir_models = '/scratch/cse/phd/anz208486/col873_project/Models' 
# dir_results = '/scratch/cse/phd/anz208486/col873_project/Results'

def load_file_to_dictionary(src_file):
	c_file = open(src_file, "rb")
	target_dictionary = pickle.load(c_file)
	c_file.close()
	return target_dictionary

# Datsets and models
# index_datasets = ['table2VecW.idx'] #dict with vectors
# bm25_ranks = ['bm25_table2VecW.idx'] #dict with top1000 tables
# query_file = os.path.join(dir_datasets,'queries.txt')
# models = ['model_train_table2VecW_final.csv']
# output_files = ['table2VecW3.out']




def score_query(dir_dataset,dir_output, query_file, index_dataset, bm25_ranks, model_file, score_file):
	query_file = os.path.join(dir_dataset,query_file)
	query_file_cursor = open(query_file)
	query_dataset = csv.reader(query_file_cursor, delimiter=" ")
	
	
	index_dataset = index_dataset
	index_filename = os.path.join(dir_output,index_dataset)
	index_dict = load_file_to_dictionary(index_filename)

	ranked_dataset = bm25_ranks
	ranked_file = os.path.join(dir_output,ranked_dataset)
	ranked_dict = load_file_to_dictionary(ranked_file)

	model_name = os.path.join(dir_output, model_file)     
	model = Doc2Vec.load(model_name)

	#open output file in write mode
	output_cursor = open(os.path.join(dir_output,score_file),'w')
	indexed_tables = set(list(index_dict.keys()))
 
	#Make query dataset & infer vectors for query
	for query in query_dataset:
		query_id = query[0]
		tables_list = set(ranked_dict[query_id]) & indexed_tables
		missing_tables = set(ranked_dict[query_id]) - tables_list
		missing_tab_list = list(missing_tables)
		print(query_id)
		print(missing_tab_list)
                
   
