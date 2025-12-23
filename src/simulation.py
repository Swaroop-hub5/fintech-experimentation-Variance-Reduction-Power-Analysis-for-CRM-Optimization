import numpy as np
import pandas as pd

def generate_experiment_data(n_users=2000, lift=0.03, noise=50):
    """
    Simulates high-variance trading data.
    - pre_period: Historical trading volume (Covariate)
    - post_period: Trading volume during experiment (Metric)
    """
    np.random.seed(42)
    
    # Generate historical 'Pre-period' data (Gamma distribution for realistic trading volume)
    pre_period = np.random.gamma(shape=2.0, scale=30.0, size=n_users)
    
    # Assign Treatment/Control groups
    group = np.random.choice(['Control', 'Treatment'], size=n_users)
    
    # Generate 'Post-period' data (correlated with pre-period + random noise)
    # This correlation is what CUPED exploits
    post_period = pre_period + np.random.normal(0, noise, size=n_users)
    
    df = pd.DataFrame({
        'user_id': range(n_users),
        'group': group,
        'pre_period': pre_period,
        'post_period': post_period
    })
    
    # Inject the 'Treatment Effect' (Lift)
    control_mean = df[df['group'] == 'Control']['post_period'].mean()
    df.loc[df['group'] == 'Treatment', 'post_period'] += (control_mean * lift)
    
    return df