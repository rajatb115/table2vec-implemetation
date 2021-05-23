from datetime import datetime
#import split_csv
#import table2VecModel
#import makeVectorIndex
#import bm25Model
import scoreQueryFull

# file_name = input("Enter the dataset name : ")
#file_name = "sp_table2VecH1.csv"
#split_filename = "table2VecH.csv"
#model_name = "model_table2VecH"
#index_files = "table2VecH.idx"
#query_file_name = "queries.txt"
#ranked_file  = "bm25_table2VecH.idx"
#output_rank_file = "table2VecH.out"

file_name = "sp_table2VecE_star.csv"
split_filename = "table2VecE_star.csv"
model_name = "model_table2VecE_star"
index_files = "table2VecE_star.idx"
query_file_name = "queries.txt"
ranked_file  = "bm25_table2VecW.idx"
output_rank_file = "table2VecE_star_Full.out"

print("Path of the file is : /scratch/cse/phd/anz208486/col873_project/NLP_project/Dataset/"+file_name)
print("Output folder path : /scratch/cse/phd/anz208486/col873_project/NLP_project/finished_output/")

output_folder = "/scratch/cse/phd/anz208486/col873_project/NLP_project/finished_output/"
input_folder = "/scratch/cse/phd/anz208486/col873_project/NLP_project/Dataset/"

# split_filename = input("Enter split file name : ")

# Spliting of the dataset.
now = datetime.now()
print("ranking started at:",now.strftime("%H:%M:%S"))

rank_file = scoreQueryFull.score_query(input_folder,output_folder,query_file_name,index_files,ranked_file,model_name,output_rank_file)

now = datetime.now()
print("ranking completed at:",now.strftime("%H:%M:%S"))

print("Ranking file location :",rank_file)
