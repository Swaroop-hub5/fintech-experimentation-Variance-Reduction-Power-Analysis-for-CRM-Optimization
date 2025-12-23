import numpy as np
import scipy.stats as stats

def get_cuped_adjusted_metric(df, metric_col, covariate_col):
    """
    Calculates the CUPED adjusted metric: Y_cuped = Y - theta * (X - E[X])
    """
    # Calculate Theta: cov(metric, covariate) / var(covariate)
    covariance_matrix = np.cov(df[metric_col], df[covariate_col])
    theta = covariance_matrix[0, 1] / np.var(df[covariate_col])
    
    # Apply adjustment
    df['cuped_metric'] = df[metric_col] - (df[covariate_col] - df[covariate_col].mean()) * theta
    return df, theta

def calculate_statistics(df, metric_col):
    """Perform a standard Welch's t-test."""
    control = df[df['group'] == 'Control'][metric_col]
    treatment = df[df['group'] == 'Treatment'][metric_col]
    
    t_stat, p_val = stats.ttest_ind(control, treatment, equal_var=False)
    variance = np.var(control)
    
    return p_val, variance