import numpy as np
import pandas as pd

def calcular_mae(y_true, y_pred):
    return np.mean(np.abs(y_true - y_pred))

def calcular_cg(rel_k):
    return np.sum(rel_k)

def calcular_dcg(rel_k):
    if len(rel_k) == 0:
        return 0.0
    posiciones = np.arange(1, len(rel_k) + 1)
    return np.sum(rel_k / np.log2(posiciones + 1))

def calcular_ndcg(rel_k, rel_total, k):
    dcg = calcular_dcg(rel_k)
    ideal_rel = np.sort(rel_total)[::-1][:k]
    idcg = calcular_dcg(ideal_rel)
    return (dcg / idcg) if idcg > 0 else 0.0

def evaluar_metricas_usuario(group, k=10):
    y_true = group['r_ui'].values
    y_pred = group['est'].values
    
    group_pred = group.sort_values(by='est', ascending=False)
    rel_k = group_pred['r_ui'].head(k).values
    
    return pd.Series({
        'MAE': calcular_mae(y_true, y_pred),
        f'CG@{k}': calcular_cg(rel_k),
        f'DCG@{k}': calcular_dcg(rel_k),
        f'NDCG@{k}': calcular_ndcg(rel_k, y_true, k)
    })