# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 19:26:18 2020

@author: Anjani Srivastava
"""

import pandas as pd
 
from sklearn.feature_extraction.text import TfidfTransformer 
from sklearn.feature_extraction.text import CountVectorizer
 
# this is a very toy example, do not try this at home unless you want to understand the usage differences
docs=["you are the only one",
      "be patient and kind to all",
      "a mouse ran away from the house",
      "honesty is the best policy",
      "be cautious always"
     ]
 
#instantiate CountVectorizer()
cv=CountVectorizer()
 
# this steps generates word counts for the words in your docs
word_count_vector=cv.fit_transform(docs)
#Prints the number of rows and unique words, repetition is avoided here
print (word_count_vector.shape)
 #Computes IDF Values
tfidf_transformer=TfidfTransformer(smooth_idf=True,use_idf=True)
tfidf_transformer.fit(word_count_vector)

# print idf values
df_idf = pd.DataFrame(tfidf_transformer.idf_, index=cv.get_feature_names(),columns=["idf_weights"])
 
# sort ascending
df_idf.sort_values(by=['idf_weights'])

# word counts for the documents in a sparse matrix form
count_vector=cv.transform(docs)
 
# tf-idf scores calculation
tf_idf_vector=tfidf_transformer.transform(count_vector)

feature_names = cv.get_feature_names()
 
#get tfidf vector for first document
first_document_vector=tf_idf_vector[0]
 
#print the scores
# Here the word 'a' is missing becauses sometimes single character is not considered by CountVectorizer
df = pd.DataFrame(first_document_vector.T.todense(), index=feature_names, columns=["tfidf"])
df.sort_values(by=["tfidf"],ascending=False)
