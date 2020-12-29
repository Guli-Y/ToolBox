import numpy as np

def get_rmse(y_true, y_pred):
    return np.sqrt(np.mean((y_true-y_pred)**2))
