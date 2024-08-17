import pandas as pd
from collections import defaultdict
import math
import json




# Tokenization (splitting text into words)
def tokenize(text):
    return text.split()  # Simple tokenization by space; you can use a more sophisticated method

# Construct Inverted Index
def inverted_indexing(documents):
    inverted_index = defaultdict(list)
    for doc_id, document in enumerate(documents):
        terms = tokenize(document)
        for term in terms:
            inverted_index[term].append(doc_id)
    return inverted_index
  
  
def save_inverted_index(inverted_index, filename):
    with open(filename, 'w') as json_file:
        json.dump(inverted_index, json_file, indent=4)