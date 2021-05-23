from datetime import datetime

import scoreQueryFull

file_name = "sp_table2VecW1.csv"
split_filename = "table2VecW.csv"
model_name = "model_table2VecW"
index_files = "table2VecW.idx"
query_file_name = "queries.txt"
ranked_file  = "bm25_table2VecW.idx"
output_rank_file = "table2VecWFull.out"

print("Path of the file is : /scratch/cse/phd/anz208486/col873_project/NLP_project/Dataset/"+file_name)
print("Output folder path : /scratch/cse/phd/anz208486/col873_project/NLP_project/output")

output_folder = "/scratch/cse/phd/anz208486/col873_project/NLP_project/output/"
input_folder = "/scratch/cse/phd/anz208486/col873_project/NLP_project/Dataset/"

# split_filename = input("Enter split file name : ")

# Spliting of the dataset.
now = datetime.now()
print("ranking started at:",now.strftime("%H:%M:%S"))

rank_file = scoreQueryFull.score_query(input_folder,output_folder,query_file_name,index_files,ranked_file,model_name,output_rank_file)

now = datetime.now()
print("ranking completed at:",now.strftime("%H:%M:%S"))

print("Ranking file location :",rank_file)
