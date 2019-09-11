import numpy as np
from scipy.interpolate import interp1d
from scipy import array
from scipy.stats import norm

cur_income = 5000.0
goal_income = 15000.0
period = 5.0
inv_time = 5
mean_rate = 0.051
sd_rate = 0.05116
# def prob_go_income(cur_income, goal_income, period, inv_time):
goal_rate = (goal_income/cur_income)**(1/period) - 1
print(goal_rate)

def rank_effort_income(inv_time):
    x = np.array([0.0,0.5,1.5,2.5,3.5,7.5,10.5,12.5,17.5,24.5])
    y = np.array([5.0,7.5,15.0,27.8,38.2,55.8,75.8,85.0,93.6,99.0])
    fl = interp1d(x,y,fill_value='extrapolate')
    rst = fl(inv_time)
    return  rst

rank_effort = rank_effort_income(inv_time)
print(rank_effort)
expected_rate= norm.ppf(rank_effort/100.0) * sd_rate + mean_rate
expected_rate = max(expected_rate, rank_effort/1000.0)
print(expected_rate)
sigma_z = (goal_rate - expected_rate)/max(expected_rate, sd_rate)
print(sigma_z)
prob_achv = 1-norm.cdf(sigma_z)
print(prob_achv)
