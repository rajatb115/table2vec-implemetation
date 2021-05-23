from datetime import datetime
import split_csv
import table2VecModel
import makeVectorIndex
import bm25Model
import scoreQuery

# file_name = input("Enter the dataset name : ")
#file_name = "sp_table2VecH1.csv"
#split_filename = "table2VecH.csv"
#model_name = "model_table2VecH"
#index_files = "table2VecH.idx"
#query_file_name = "queries.txt"
#ranked_file  = "bm25_table2VecH.idx"
#output_rank_file = "table2VecH.out"

file_name = "sp_table2VecW1.csv"
split_filename = "table2VecW.csv"
model_name = "model_table2VecW"
index_files = "table2VecW.idx"
query_file_name = "queries.txt"
ranked_file  = "bm25_table2VecW.idx"
output_rank_file = "table2VecW.out"

print("Path of the file is : /scratch/cse/phd/anz208486/col873_project/NLP_project/Dataset/"+file_name)
print("Output folder path : /scratch/cse/phd/anz208486/col873_project/NLP_project/output")

output_folder = "/scratch/cse/phd/anz208486/col873_project/NLP_project/output"
input_folder = "/scratch/cse/phd/anz208486/col873_project/NLP_project/Dataset/"

# split_filename = input("Enter split file name : ")

# Spliting of the dataset.
# now = datetime.now()
# print("Spliting the file started at:",now.strftime("%H:%M:%S"))

# train_dataset,test_dataset =  split_csv.split_fun(input_folder, output_folder, file_name, split_filename)

# now = datetime.now()
# print("Spliting the file completed at:",now.strftime("%H:%M:%S"))

# print("Location of train dataset :",train_dataset)
# print("Location of test dataset :",test_dataset)

# Creating the model
# now = datetime.now()
# print("Model creation started at:",now.strftime("%H:%M:%S"))

# model_file = table2VecModel.Tab2Vec_train(model_name,train_dataset,output_folder)

# now = datetime.now()
# print("Model creation completed at:",now.strftime("%H:%M:%S"))

# print("Location of Model file :",model_file)


now = datetime.now()
print("Vectorization started at:",now.strftime("%H:%M:%S"))

vector_file = makeVectorIndex.indexing(index_files,input_folder,file_name,model_name,output_folder )

now = datetime.now()
print("Vectorization completed at:",now.strftime("%H:%M:%S"))

print("Location of vector :",vector_file)

#now = datetime.now()
#print("bm25 started at:",now.strftime("%H:%M:%S"))


#bm25_file = bm25Model.bm25(input_folder,query_file_name, file_name, ranked_file, output_folder )

#now = datetime.now()
#print("bm25 completed at:",now.strftime("%H:%M:%S"))

#print("BM25 file location :",bm25_file)

#now = datetime.now()
#print("ranking started at:",now.strftime("%H:%M:%S"))

#rank_file = scoreQuery.score_query(input_folder,output_folder,query_file_name,index_files,ranked_file,model_name,output_rank_file)

#now = datetime.now()
#print("ranking completed at:",now.strftime("%H:%M:%S"))
#
#print("Ranking file location :",rank_file)
