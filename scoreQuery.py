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




def score_query(dir_dataset,dir_output, query_file, index_dataset, bm25_ranks, model_file,score_file):
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
		query_txt = query[1:]
		inferred_queryVec  = model.infer_vector(query_txt,alpha=0.1,epochs=100)
		sim_score_list = []
		tables_list = list(set(ranked_dict[query_id]) & indexed_tables)
                
		#print(tables_list)
		for table_id in tables_list:
			#print(table_id)
			cs = cosine_similarity(index_dict[table_id].reshape(1,-1),inferred_queryVec.reshape(1,-1))[0][0]
			#print(cs)
			sim_score_list.append(cs)
		tables_array = np.array(tables_list)
		sim_score_array = np.array(sim_score_list)
		indexes = np.flip(np.argsort(sim_score_array))
		sorted_tables = np.array(tables_array)[indexes]
		sorted_sim_scores = np.array(sim_score_array)[indexes]
		ranked_tables = sorted_tables.tolist()
		ranked_scores = sorted_sim_scores.tolist()
		for j in range(1000):            
			ranked_table_id = ranked_tables[j]
			sim_score =  str(ranked_scores[j])
			line = query_id+'\tQ0\t'+ranked_table_id+'\t'+str(j+1)+'\t'+sim_score+'\t'+'RUN2'+'\n'
			output_cursor.write(line)
	output_cursor.close()
	query_file_cursor.close()
	return os.path.join(dir_output,score_file)

      
# score_query(dir_dataset,dir_output, query_file, index_dataset, bm25_ranks, model_file,score_file)
# print (score_query("/scratch/cse/phd/anz208486/col873_project/NLP_project/Dataset/","/scratch/cse/phd/anz208486/col873_project/NLP_project/output","queries.txt","table2VecH.idx","bm25_table2VecH.idx","table2VecH","score.out"))

        #sort cs descending and list top1000 tables
   
