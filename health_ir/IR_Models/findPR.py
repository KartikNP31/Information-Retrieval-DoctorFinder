
import matplotlib.pyplot as plt
import numpy as np
import json

# Relevance data: Document IDs and their relevance

# relevance_data = {
#     "1193": 1, "1212": 1, "1273": 0, "1304": 1, "1310": 0, "1326": 1, "1331": 1,
#     "1384": 1, "1388": 1, "1433": 1, "1456": 0, "1463": 0, "1473": 1, "1496": 1,
#     "1514": 0, "1540": 0, "1547": 0, "1550": 1, "1568": 1, "1580": 1
# }

def findPR(relevance_data):
    # print(type(relevance_data))
    print(relevance_data)
    total_relevant = 40
    total_documents = 30000

    # Calculating precision and recall values
    precision_values = []


    recall_values = []
    relevant_docs_retrieved = 0
    relevant_docs_found = 0

    for doc_id, relevance in relevance_data.items():
        if relevance == 1:
            relevant_docs_found += 1

        relevant_docs_retrieved += relevance
        precision = relevant_docs_retrieved / (
            len(precision_values) + 1
        )  # Adding 1 to prevent division by zero
        recall = relevant_docs_retrieved / total_relevant

        precision_values.append(precision)
        recall_values.append(recall)

    # to cal. interpolated points
    interpolated_recall = np.linspace(0, 1, num=11)
    interpolated_precision = []

    for interp_r in interpolated_recall:
        precisions_at_recall = [
            prec for rec, prec in zip(recall_values, precision_values) if rec >= interp_r
        ]
        interpolated_precision.append(
            max(precisions_at_recall) if precisions_at_recall else 0
        )

    # plot the P-R curve with interpolated points 
    plt.figure(figsize=(8, 6))
    plt.plot(recall_values, precision_values, marker="o", linestyle="-", label="P-R Curve")
    plt.plot(
        interpolated_recall,
        interpolated_precision,
        marker="x",
        linestyle="",
        color="red",
        label="Interpolated Points",
    )

    plt.xlabel("Recall")
    plt.ylabel("Precision")
    plt.title("Precision-Recall Curve with Interpolated Points")
    plt.legend()
    plt.grid(True)
    plt.show()
    
    
    
    
    
# relevance_data = {"1193":0,"1212":1,"1273":1,"1304":0,"1310":1,"1326":0,"1331":0,"1384":1,"1388":0,"1433":1,"1456":0,"1463":1,"1473":0,"1496":1,"1514":0,"1540":0,"1547":0,"1550":1,"1568":1,"1580":0}
# findPR(relevance_data)
