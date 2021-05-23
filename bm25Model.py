#Import the required libraries
from rank_bm25 import BM25Okapi
import csv
import os
import pickle
import sys

csv.field_size_limit(sys.maxsize)
#save dictionary to file

def save_dictionary(dict_to_save,pickle_dict_name):
	c_file = open(pickle_dict_name, "wb")
	pickle.dump(dict_to_save, c_file,-1)
	c_file.close()

# query_file_name = 'queries.txt'
#files = ['table2vecH.csv','table2vecW.csv']
# files = ['table2VecW_final.csv']
# ranked_files  = ['bm25_table2VecW.idx']
#files = ['table2VecW_final.csv']
#ranked_files  = ['bm25_table2VecW.idx']


def bm25(dataset_location, query_file_name, dataset_file,ranked_file,output_location ):

	# query_file = open(os.path.join('/scratch/cse/phd/anz208486/col873_project/Datasets',query_file_name))
	query_file = open(os.path.join(dataset_location, query_file_name))
	queries = csv.reader(query_file, delimiter=" ")
	output_folder = output_location 
	# Loading the dataset and the model from the drive.
	file_name = dataset_file
		
	filename = open(os.path.join(dataset_location,file_name))
	dataset = csv.reader(filename, delimiter="\t")
	corpus = []
	tokenized_corpus = [] #tokenized information for each table
	for doc in dataset:
		if len(doc)>1:
			corpus.append(doc[0]) 
			tokenized_corpus.append(doc[1].split(" "))
	filename.close()
	bm25 = BM25Okapi(tokenized_corpus)

    	# We can process query file to have query_id, query and tokenized_query, save it as a pickled csv file
	
	topK_docs = {} #dictionary to save top1000 documents with query_id as key
	
	for query in queries: 
		query_id = query[0]
		tokenized_query = query[1:]
		doc_scores = bm25.get_scores(tokenized_query)
		top_docs = bm25.get_top_n(tokenized_query, corpus, n=100000)
		topK_docs[query_id] = top_docs
	ranked_file_name = os.path.join(output_folder,ranked_file)
	print(ranked_file_name)
	save_dictionary(topK_docs,ranked_file_name)
	query_file.close()
	return ranked_file_name


#print(bm25("/scratch/cse/phd/anz208486/col873_project/NLP_project/Dataset/", "queries.txt", "sp_table2VecW1.csv","bm25_table2VecW.idx","/scratch/cse/phd/anz208486/col873_project/NLP_project/output" ))
#save_dictionary(top1000_docs,'../Datasets/original_rankings')    
