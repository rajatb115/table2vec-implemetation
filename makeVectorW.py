from datetime import datetime
#import split_csv
#import table2VecModel
import makeVectorIndex
#import bm25Model
#import scoreQuery


file_name = "sp_table2VecW1.csv"
split_filename = "table2VecW.csv"
model_name = "model_table2VecW"
index_files = "table2VecW.idx"
query_file_name = "queries.txt"
ranked_file  = "bm25_table2VecW.idx"
output_rank_file = "table2VecW.out"

print("Path of the file is : /scratch/cse/phd/anz208486/col873_project/NLP_project/Dataset/"+file_name)
print("Output folder path : /scratch/cse/phd/anz208486/col873_project/NLP_project/finished_output")

output_folder = "/scratch/cse/phd/anz208486/col873_project/NLP_project/finished_output"
input_folder = "/scratch/cse/phd/anz208486/col873_project/NLP_project/Dataset/"


now = datetime.now()
print("Vectorization started at:",now.strftime("%H:%M:%S"))

vector_file = makeVectorIndex.indexing(index_files,input_folder,file_name,model_name,output_folder )

now = datetime.now()
print("Vectorization completed at:",now.strftime("%H:%M:%S"))
