#Code to create train models
#Import required packages

#import pandas as pd
import csv
import sys
import os
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from sklearn.metrics.pairwise import cosine_similarity

csv.field_size_limit(sys.maxsize)
    
def Tab2Vec_train(file_name, trainfile, location):
    

    # Loading the dataset.
            #tokenized_corpus.append(doc[1].split(" "))

    #filename = open('/scratch/cse/phd/anz208486/col873_project/Datasets/' + file_name)
    filename = open(trainfile)
    dataset = csv.reader(filename, delimiter="\t")
    
    # Creating the documents.
    # doc[1] is the document, if present we want to vectorize and rest of the fields are used to create a tag
    documents = [] 
    for doc in dataset:
        if len(doc)>1:
            #documents.append(doc[1].split(" "))
            documents.append(TaggedDocument(doc[1].split(" "),[doc[0]]))
    print('Documents Collected.')
    filename.close()  
    #Declaring the DT2V Model
    model = Doc2Vec(vector_size=50,window=3,min_count=3,alpha=0.1,min_alpha=0.001)
    print('Model Initialized.')
    #print(len(documents))    
    #print(documents[10])
    # Building vocabulary.
    model.build_vocab(documents)
    #print('Vocabulary size: ',len(model.wv.vocab.keys()))
    
    # Training model.
    for epoch in range(1,101):
        model.train(documents,total_examples=len(documents),epochs=1)
        if epoch==1 or epoch%10==0:
            print('Epoch :',epoch, cosine_similarity([model.dv[94],model.dv[519]])[0][1])
    print('Model Trained.')
    
    # Saving model.
    #file = open('/scratch/cse/phd/anz208486/col873_project/Models/model_'+file_name,'wb')
    f = os.path.join(location, file_name)
    file = open(f,'wb')
    model.save(file)
    file.close()
    print('Model Saved.\\n\\n')
    return f


  
#for file_name in ['train_table2VecW_final.csv']:
#, train_table2VecH_final.csv]:
#    Tab2Vec_train(file_name)
   
