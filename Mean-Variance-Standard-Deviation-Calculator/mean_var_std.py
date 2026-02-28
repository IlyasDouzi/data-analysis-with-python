import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    
    M = np.array(list).reshape(3, 3)

    mean_l = np.mean(M, axis=1).tolist()
    var_l = np.var(M, axis=1).tolist()
    std_dev_l = np.std(M, axis=1).tolist()
    max_l = np.max(M, axis=1).tolist()
    min_l = np.min(M, axis=1).tolist()
    sum_l = np.sum(M, axis=1).tolist()

    mean_c = np.mean(M, axis=0).tolist()
    var_c = np.var(M, axis=0).tolist()
    std_dev_c = np.std(M, axis=0).tolist()
    max_c = np.max(M, axis=0).tolist()
    min_c = np.min(M, axis=0).tolist()
    sum_c = np.sum(M, axis=0).tolist()

    list_mean = np.mean(list).item()
    list_var = np.var(list).item()
    list_std = np.std(list).item()
    list_max = np.max(list).item()
    list_min = np.min(list).item()
    list_sum = np.sum(list).item()

    calculations = {
        'mean': [mean_c, mean_l, list_mean],
        'variance': [var_c, var_l, list_var],
        'standard deviation': [std_dev_c, std_dev_l, list_std],
        'max': [max_c, max_l, list_max],
        'min': [min_c, min_l, list_min],
        'sum': [sum_c, sum_l, list_sum]
    }

    return calculations