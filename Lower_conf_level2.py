import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import scipy.stats as stats
import statsmodels as stmd

def compute_lower_bound(n, mu, stdev, z):
    """
    Computes lower bound of a confidence interval
    Parameters:
        n: Type int. number of data points
        mu: Type float. sample mean
        stdev: Type float. sample standard deviation
        z: Type float. critical value. Default to 95%CI that corresponds to value of 1.96
    """

    return mu - stats.norm.ppf(z) * (stdev / (n ** 0.5))

n = int(input("Enter the number of data points: "))
mu = float(input("Enter the sample mean: "))
stdev = float(input("Enter the sample standard deviation: "))
z = float(input("Enter the critical value (press enter for default 95% CI value): ") or 0.975)

    
lower_bound = compute_lower_bound(n, mu, stdev, z)
print("The lower bound of the confidence interval is:", lower_bound)
