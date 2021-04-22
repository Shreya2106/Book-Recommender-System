import pandas as pd
import numpy as np
from sklearn.neighbors._unsupervised import NearestNeighbors
from scipy.sparse import csr_matrix

final_rating=pd.read_csv('model/FinalRating.csv')

book_pivot=final_rating.pivot_table(columns='user_id', index='title', values='rating')
book_pivot.fillna(0, inplace=True)

book_sparse=csr_matrix(book_pivot)

models=NearestNeighbors(metric='cosine', algorithm='brute')
models.fit(book_sparse)

def recommend(book_name):
    book_id = np.where(book_pivot.index == book_name)[0][0]
    distances, suggestions = models.kneighbors(book_pivot.iloc[book_id, :].values.reshape(1, -1),n_neighbors=6)
    y=[]
    for i in range(len(suggestions.flatten())):
        if i==0:
            continue
        else:
            y.append(book_pivot.index[suggestions.flatten()[i]])
    return y