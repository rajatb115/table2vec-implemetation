# Importing the required libraries.
import numpy as np
#import pickle, zlib
from random import sample
import scipy.cluster.hierarchy as sch
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from gensim.models.keyedvectors import KeyedVectors
from sklearn.metrics.pairwise import cosine_similarity
from gensim import corpora
import pandas as pd
        
import gensim
import os
import pickle


 
#dir_datasets = '/scratch/cse/phd/anz208486/col873_project/Datasets'     
#dir_models = '/scratch/cse/phd/anz208486/col873_project/Models' 

# Datsets and models
#train_datasets = ['train_table2VecW_final.csv']
#test_datasets = ['test_table2VecW_final.csv']

#tables_datasets = ['table2VecW_final.csv']
#models = ['model_train_table2VecW_final.csv']
#index_files = ['table2VecW.idx']

#save the dictionaries to the disk
def save_dictionary(dict_to_save,output_path, pickle_dict_name):
    #complete_file_name = os.path.join(dir_datasets,pickle_dict_name)
    complete_file_name = os.path.join(output_path,pickle_dict_name)
    c_file = open(complete_file_name, "wb")
    pickle.dump(dict_to_save, c_file,-1)
    c_file.close()
    return complete_file_name

#for i in range(len(tables_datasets)):
def indexing(index_file, dir_dataset, file_name, model_name, output_path):
 
    index_filename = index_file
    dict_index = {}

    tables_filename = os.path.join(dir_dataset,file_name)
    tables_df = pd.read_csv(tables_filename, sep='\t', header=None)
 
    model_name = os.path.join(output_path,model_name)
    model = Doc2Vec.load(model_name)
    for table in tables_df.iterrows():
        txt_str = str(table[1][1])
        txt = txt_str.split(" ")
        inferred_tableVec = model.infer_vector(txt,alpha=0.1,epochs=100)
        dict_index[table[1][0]] = inferred_tableVec
        #print(dict_index[table[1][0]])
        #break
    return save_dictionary(dict_index,output_path, index_filename)   
