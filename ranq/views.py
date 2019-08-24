from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Question, Rank_Income, Info_Income, U_Info_Income
from .forms import QuestionForm, Short_answerForm, Income_answerForm
import numpy as np
from scipy.interpolate import interp1d
from scipy import array

# Create your views here.
def question_list(request):
    questions = Question.objects.all()
    return render(request, 'ranq/question_list.html', {'questions':questions})

# 주관식에 관한 것 하나만 해봄
def question_detail(request, pk):
    q = get_object_or_404(Question, pk=pk)
    c = q.id
    # post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = Short_answerForm(request.POST)
        # form2 = Income_answerForm(request.POST)
        if form.is_valid():
            ans = form.save(commit=False)
            ans.output = rank_earning(float(ans.answer))
            ans.question_id = c
            a = ans
            ans.save()

            ## 결과 페이지로 가는 것으로 수정해야함 2019.08.07 수정
            # return redirect('question_list') #, pk=post.pk)
            return render(request,  'ranq/question_a_result.html',{'q':q, 'a': a})

    else:
        form = Short_answerForm()
    return render(request,  'ranq/question_detail.html',{'q':q, 'form': form})

#@login_required
def question_new(request):
    if request.method == "POST":
        form = QuestionForm(request.POST, request.FILES)
        if form.is_valid():
            q = form.save(commit=False)
            q.author = request.user
            #post.published_date = timezone.now()
            q.save()
            return redirect('question_detail', pk=q.pk)
    else:
        form = QuestionForm()
    return render(request, 'ranq/question_edit.html',{'form':form})

# 소득 분위 추정 2018 기준

# 주관식에 관한 것 하나만 해봄
def t_question_detail(request, pk):
    q = get_object_or_404(Question, pk=pk)
    c = q.id
    # post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = Income_answerForm(request.POST)
        if form.is_valid():
            ans = form.save(commit=False)
            ans.rank_income = rank_earning(ans.y_income)
            ans.m_income = income_details(ans.y_income)[0]
            ans.de_income	=	income_details(ans.y_income)[1]
            ans.de_amount	=	income_details(ans.y_income)[2]
            ans.na_pension	=	income_details(ans.y_income)[3]
            ans.he_insurance	=	income_details(ans.y_income)[4]
            ans.a_insurance	=	income_details(ans.y_income)[5]
            ans.em_insurance	=	income_details(ans.y_income)[6]
            ans.in_tax	=	income_details(ans.y_income)[7]
            ans.resi_tax	=	income_details(ans.y_income)[8]

            a = ans
            b = income_details(ans.y_income)[3] + income_details(ans.y_income)[4] +  income_details(ans.y_income)[5] +  income_details(ans.y_income)[6] #insurance total
            c = income_details(ans.y_income)[7] + income_details(ans.y_income)[8] #tax total
            ans.save()
            ## 결과 페이지로 가는 것으로 수정해야함 2019.08.07 수정
            # return redirect('question_list') #, pk=post.pk)
            return render(request,  'ranq/t_question_a_result.html',{'q':q, 'a': a,'b':b, 'c':c})

    else:
        form = Income_answerForm()
    return render(request,  'ranq/t_question_detail.html',{'q':q, 'form': form})

def t_question_list(request):
    questions = Question.objects.all()
    return render(request, 'ranq/t_question_list.html', {'questions':questions})

def rank_earning(earning):
    rank_income = Rank_Income.objects.all()
    x = np.array([])
    y = np.array([])
    for f in rank_income:
        x = np.append(x, f.rank)
        y = np.append(y, f.y_income)
    fl = interp1d(y,x)
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
