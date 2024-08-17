import pandas as pd
from collections import defaultdict
import math
import json



from health_ir.IR_Models.InvertedIndexing import tokenize
from health_ir.IR_Models.CosineSimilarity import cosine_similarity
from health_ir.IR_Models.InvertedIndexing import save_inverted_index
from health_ir.IR_Models.TF_IDF import save_tfidf_values , save_values

def retrieve_documents_with_info(query, inverted_index, documents_tfidf, documents, data, idf_values, tf_values):
    relevant_doc_ids = set()
    query_terms = tokenize(query)
    for term in query_terms:
        if term in inverted_index:
            relevant_doc_ids.update(inverted_index[term])
    relevant_doc_ids = list(relevant_doc_ids)
    
    similarity_scores = cosine_similarity(query, [documents_tfidf[i] for i in relevant_doc_ids])
    
    document_similarity = list(zip(relevant_doc_ids, similarity_scores))
    sorted_documents = sorted(document_similarity, key=lambda x: x[1], reverse=True)
    
    top_n_results = 20  # top 20 doc retrieving
    top_documents_indices = [doc_index for doc_index, _ in sorted_documents[:top_n_results]]
    
    relevant_data = data.iloc[top_documents_indices]
    
    relevant_docs_formatted = []
    for index, row in relevant_data.iterrows():
        doc_info = {
            "DocumentID": index,
            "DoctorName": row['DoctorName'],
            "Experience": row['Experience'],
            "Speciality": row['Speciality'],
            "Fees": row['Fees'],
            "Rating": row['Rating'],
            "Locality": row['Locality'],
            "City": row['City']
        }
        relevant_docs_formatted.append(doc_info)
    

    save_inverted_index(inverted_index, 'health_ir/IR_Models/inverted_index.json')
    save_tfidf_values(documents_tfidf, 'health_ir/IR_Models/tfidf_values.json')
    save_values(documents_tfidf, idf_values, tf_values, 'health_ir/IR_Models/values.json')

    return relevant_docs_formatted
