import statsmodels.stats.power as TTestPower
import numpy as np

def calculate_required_sample_size(baseline_mean, baseline_std, mde, alpha=0.05, power=0.80):
    """
    Calculates the required sample size per group.
    - mde: Minimum Detectable Effect (as a decimal, e.g., 0.02 for 2%)
    """
    # Effect size (Cohen's d) = (Mean1 - Mean2) / Pooled Standard Deviation
    # For a relative lift, Mean2 = Mean1 * (1 + mde)
    effect_size = (baseline_mean * mde) / baseline_std
    
    analysis = TTestPower.TTestIndPower()
    sample_size = analysis.solve_power(
        effect_size=effect_size, 
        power=power, 
        alpha=alpha, 
        ratio=1.0, 
        alternative='two-sided'
    )
    
    return int(np.ceil(sample_size))