import pandas as pd

from health_ir.IR_Models.InvertedIndexing import inverted_indexing
from health_ir.IR_Models.TF_IDF import calculate_tf, calculate_idf, calculate_tfidf, getData
from health_ir.IR_Models.RetriveDoc import retrieve_documents_with_info





def mainQuerySearch(query):
    info = pd.read_csv('health_ir\IR_Models\Data.csv').head(47000)
    # print(data)
    
    data = getData(info)
    data['Speciality'] = data['Speciality'].fillna('') 

    # Combining 'city', 'locality', and 'Speciality' columns into a single document
    data['document'] = data['City'].str.lower() + ' ' + data['Locality'].str.lower() + ' ' + data['Speciality'].str.lower()

    documents = data['document'].tolist()
    inverted_index = inverted_indexing(documents)
    documents_tfidf = calculate_tfidf(data)
    idf_values = calculate_idf(data['document'])
    tf_values = [calculate_tf(document) for document in data['document']]
    relevant_docs = retrieve_documents_with_info(query, inverted_index, documents_tfidf, documents, data, idf_values, tf_values)
    # print(relevant_docs)
    return relevant_docs
