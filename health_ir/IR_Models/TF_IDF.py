import pandas as pd
from collections import defaultdict
import math
import json


from health_ir.IR_Models.InvertedIndexing import tokenize



def getData(data) : 
    return data.head(47000)
# Calculate TF for each term in each document
def calculate_tf(document):
    words = tokenize(document)
    word_count = len(words)
    term_freq = {}
    for word in words:
        term_freq[word] = term_freq.get(word, 0) + 1
    for word in term_freq:
        term_freq[word] = term_freq[word] / word_count
    return term_freq

# Calculate IDF for each term in all documents
def calculate_idf(documents):
    total_documents = len(documents)
    idf = {}
    for document in documents:
        words = set(tokenize(document))
        for word in words:
            idf[word] = idf.get(word, 0) + 1
    for word in idf:
        idf[word] = math.log10(total_documents / (1 + idf[word]))
    return idf

# Calculate TF-IDF for documents
def calculate_tfidf(data):
    documents = data['document']
    tfidf_scores = []
    idf = calculate_idf(documents)
    for document in documents:
        tf = calculate_tf(document)
        tfidf = {word: tf[word] * idf[word] for word in tf}
        tfidf_scores.append(tfidf)
    return tfidf_scores
  
def save_tfidf_values(tfidf_values, filename):
    with open(filename, 'w') as json_file:
        json.dump(tfidf_values, json_file, indent=4)
        
        
def save_values(tfidf_values, idf_values, tf_values, filename):
    data = {
        'TF-IDF': tfidf_values,
        'IDF': idf_values,
        'TF': tf_values
    }
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)
        
