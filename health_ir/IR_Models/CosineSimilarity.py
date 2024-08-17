import pandas as pd
from collections import defaultdict
import math
import json


from health_ir.IR_Models.TF_IDF import calculate_tf 


# cosine similarity between the query and documents
def cosine_similarity(query, documents_tfidf):
    query_tfidf = calculate_tf(query)
    similarity_scores = []
    for doc_tfidf in documents_tfidf:
        dot_product = sum(query_tfidf[word] * doc_tfidf.get(word, 0) for word in query_tfidf)
        query_norm = math.sqrt(sum(query_tfidf[word]**2 for word in query_tfidf))
        doc_norm = math.sqrt(sum(doc_tfidf[word]**2 for word in doc_tfidf))
        cosine_sim = dot_product / (query_norm * doc_norm) if (query_norm * doc_norm) != 0 else 0
        similarity_scores.append(cosine_sim)
    return similarity_scores