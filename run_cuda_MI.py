import cupy as cp
import pandas as pd
import cudf
from cuml.metrics import mutual_info_score
import time
import numpy as np
from sklearn.preprocessing import LabelEncoder

def delete_zeroes(file_path, axis = 1, sep = "\t", index_col = 0):
    # axis = 1 for columns, axis = 0 for rows
    df_gpu = cudf.read_csv(file_path, sep=sep, index_col=index_col)
    try:
        if axis not in [0, 1]:
            raise ValueError("Invalid axis value. Use 1 for columns or 0 for rows.")
        if axis == 0:
            df_gpu = df_gpu.transpose()
    except ValueError as e:
        print(e)
        return None
    df_gpu["sum"] = df_gpu.sum(axis = 1)
    df_gpu = df_gpu.query("sum != 0.0")
    df_gpu = df_gpu.drop(columns=["sum"])
    df_gpu = df_gpu.transpose()
    return df_gpu

def simplify_labels(file_path):
    df = pd.read_csv(file_path, sep=",", index_col=0)
    le = LabelEncoder()
    for col in df.columns:
        df[col] = le.fit_transform(df[col])
    return df

def create_mi_matrix(df):
    n_features = df.shape[1]
    print(n_features)
    mi_matrix = cp.zeros((n_features, n_features), dtype=cp.float32)
    cp.fill_diagonal(mi_matrix, 10.0)
    for i in range(n_features):
        x = cp.asarray(df.iloc[:, i].values)
        for j in range(i+1, n_features):  
            y = cp.asarray(df.iloc[:, j].values)
            score = mutual_info_score(x, y)
            mi_val = cp.float32(score)
            mi_matrix[i, j] = mi_matrix[j, i] = mi_val
    mi_df = cudf.DataFrame(mi_matrix, columns=df.columns, index=df.columns)
    return mi_df
