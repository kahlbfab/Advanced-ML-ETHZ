import pandas as pd

def nice_results(cv_results):
    '''
    Retunrns the sorted crossvalidation results
    '''
    df_cv_results = pd.DataFrame(cv_results)
    df_cv_results = df_cv_results[[
    'rank_test_score',
    'params',
    'mean_test_score',
    'std_test_score'
    ]].sort_values(['rank_test_score'])
    
    return df_cv_results