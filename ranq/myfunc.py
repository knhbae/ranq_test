import numpy as np
from scipy.interpolate import interp1d
from scipy import array
from scipy.stats import norm
from .models import Question, Rank_Income, Info_Income, U_Info_Income

#노력 대비 목표 임금 달성 가능성 계산기
def prob_go_income(cur_income, goal_income, period, inv_time):
    #average income growth rate
    mean_rate = 0.051
    #standard deviation income growth rate
    sd_rate = 0.05116
    #average rate of goal income growth
    goal_rate = (goal_income/cur_income)**(1/period) - 1
    #노력시간에 대한 Rank
    rank_effort = rank_effort_income(inv_time)
    #노력시간에 따른 예상 임금 상승률
    expected_rate = norm.ppf(rank_effort/100.0) * sd_rate + mean_rate
    #보정
    expected_rate = max(expected_rate, rank_effort/1000.0)
    #z분포에서의 x sigma값
    sigma_z = (goal_rate - expected_rate)/max(expected_rate, sd_rate)
    #달성가능성
    prob_achv = 1-norm.cdf(sigma_z)

    return prob_achv

#노력시간에 대한 Rank (prob_go_income 보조 함수)
def rank_effort_income(inv_time):
    x = np.array([0.0,0.5,1.5,2.5,3.5,7.5,10.5,12.5,17.5,24.5])
    y = np.array([5.0,7.5,15.0,27.8,38.2,55.8,75.8,85.0,93.6,99.0])
    fl = interp1d(x,y,fill_value='extrapolate')
    rst = fl(inv_time)
    return  rst

def rank_earning(earning):
    rank_income = Rank_Income.objects.all()
    x = np.array([])
    y = np.array([])
    for f in rank_income:
        x = np.append(x, f.rank)
        y = np.append(y, f.y_income)
    fl = interp1d(y,x,fill_value='extrapolate')
    if earning > np.max(y)/10000.0:
        rst = np.min(x)
    elif earning < np.min(y)/10000.0:
        rst = np.max(x)
    else:
        rst = np.round_(fl(earning*10000.0),2)
    return rst

def income_details(income):
    rst =	np.array([])
    info_income = Info_Income.objects.all()
    y_income	=	np.array([])
    m_income	=	np.array([])
    de_income	=   np.array([])
    de_amount	=	np.array([])
    na_pension	=	np.array([])
    he_insurance	=	np.array([])
    a_insurance	=	np.array([])
    em_insurance	=	np.array([])
    in_tax	=	np.array([])
    resi_tax =	np.array([])

    for f in info_income:
        y_income	=	np.append(y_income, f.y_income)
        m_income	=	np.append(m_income, f.m_income)
        de_income	=   np.append(de_income, f.de_income)
        de_amount	=	np.append(de_amount, f.de_amount)
        na_pension	=	np.append(na_pension, f.na_pension)
        he_insurance	=	np.append(he_insurance, f.he_insurance)
        a_insurance	=	np.append(a_insurance, f.a_insurance)
        em_insurance	=	np.append(em_insurance, f.em_insurance)
        in_tax	=	np.append(in_tax, f.in_tax)
        resi_tax =	np.append(resi_tax, f.resi_tax)
    # fl = intp(y_income,m_income)
    fl = interp1d(y_income,m_income,fill_value='extrapolate')
    rst = np.append(rst, np.round_(fl(income*10000.0)/10000.0,0))
    fl = interp1d(y_income,de_income,fill_value='extrapolate')
    rst = np.append(rst, np.round_(fl(income*10000.0)/10000.0,0))
    fl = interp1d(y_income,de_amount,fill_value='extrapolate')
    rst = np.append(rst, np.round_(fl(income*10000.0)/10000.0,0))
    fl = interp1d(y_income,na_pension,fill_value='extrapolate')
    rst = np.append(rst, np.round_(fl(income*10000.0)/10000.0,0))
    fl = interp1d(y_income,he_insurance,fill_value='extrapolate')
    rst = np.append(rst, np.round_(fl(income*10000.0)/10000.0,0))
    fl = interp1d(y_income,a_insurance,fill_value='extrapolate')
    rst = np.append(rst, np.round_(fl(income*10000.0)/10000.0,0))
    fl = interp1d(y_income,em_insurance,fill_value='extrapolate')
    rst = np.append(rst, np.round_(fl(income*10000.0)/10000.0,0))
    fl = interp1d(y_income,in_tax,fill_value='extrapolate')
    rst = np.append(rst, np.round_(fl(income*10000.0)/10000.0,0))
    fl = interp1d(y_income,resi_tax,fill_value='extrapolate')
    rst = np.append(rst, np.round_(fl(income*10000.0)/10000.0,0))

    return rst
