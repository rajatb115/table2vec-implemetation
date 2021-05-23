from datetime import datetime
#import split_csv
#import table2VecModel
#import makeVectorIndex
import bm25Model
#import scoreQuery

# file_name = input("Enter the dataset name : ")
#file_name = "sp_table2VecH1.csv"
#split_filename = "table2VecH.csv"
#model_name = "model_table2VecH"
#index_files = "table2VecH.idx"
#query_file_name = "queries.txt"
#ranked_file  = "bm25_table2VecH.idx"
#output_rank_file = "table2VecH.out"

file_name = "sp_table2VecW1.csv"
split_filename = "table2VecW1.csv"
model_name = "model_table2VecW"
index_files = "table2VecW.idx"
query_file_name = "queries.txt"
ranked_file  = "bm25_table2VecW_1L.idx"
output_rank_file = "table2VecW.out"

print("Path of the file is : /scratch/cse/phd/anz208486/col873_project/NLP_project/Dataset/"+file_name)
print("Output folder path : /scratch/cse/phd/anz208486/col873_project/NLP_project/finished_output")

output_folder = "/scratch/cse/phd/anz208486/col873_project/NLP_project/finished_output"
input_folder = "/scratch/cse/phd/anz208486/col873_project/NLP_project/Dataset/"

# split_filename = input("Enter split file name : ")

# Spliting of the dataset.
now = datetime.now()
print("bm25 started at:",now.strftime("%H:%M:%S"))


bm25_file = bm25Model.bm25(input_folder,query_file_name, file_name, ranked_file, output_folder )

now = datetime.now()
print("bm25 completed at:",now.strftime("%H:%M:%S"))

print("BM25 file location :",bm25_file)

