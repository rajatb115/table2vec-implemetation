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
 
def load_file_to_dictionary(src_file):
	c_file = open(src_file, "rb")
	target_dictionary = pickle.load(c_file)
	c_file.close()
	return target_dictionary

	
dir_output = '/scratch/cse/phd/anz208486/col873_project/NLP_project/finished_output'
#ranked_dataset = 'bm25_table2VecW.idx'
ranked_dataset = 'bm25_table2VecW_1L.idx' 
ranked_filename = os.path.join(dir_output,ranked_dataset)
#print(ranked_filename)
c_file = open(ranked_filename, "rb")
ranked_dict = pickle.load(c_file) 
#ranked_dict = load_file_to_dictionary(ranked_filename)
queries = list(ranked_dict.keys())
#print(queries)

output_file = os.path.join(dir_output,'bm_ranks_1L.out')
output_cursor = open(output_file,'w')

queries = list(ranked_dict.keys())
print(queries)

for query_id in queries:
    j = 0
    tables = ranked_dict[query_id]
    #print(tables)
    for table_id in tables:
        line = query_id+'\tQ0\t'+table_id+'\t'+str(j+1)+'\t0.0\t\RUN4\n'
        j = j+1
        output_cursor.write(line)
output_cursor.close()
c_file.close()
  
#line = query_id+'\tQ0\t'+table_id+'\t'+str(j+1)+'\t0.0\tRUN3\n'
#j = j+1
 
