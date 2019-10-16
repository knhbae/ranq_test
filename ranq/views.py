from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Question, Rank_Income, Info_Income, U_Info_Income, Goal_Income, Endure_Test, Iq_Questions, Iq_Answers
from .forms import QuestionForm, Short_answerForm, Income_answerForm, Goal_IncomeForm, Endure_TestForm, Iq_QuestionsForm, Iq_AnswersForm
import numpy as np
from scipy.interpolate import interp1d
from scipy import array
from .myfunc import rank_earning, income_details, prob_go_income

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

def test_income(request):
    q = get_object_or_404(Question, pk=2)
    # c = q.id
    # post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = Income_answerForm(request.POST)
        if form.is_valid():
            ans = form.save(commit=False)
            ans.rank_income = rank_earning(ans.y_income)
            ans.rank_income = np.round_(ans.rank_income,1)
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
            return render(request,  'ranq/test_income_result.html',{'q':q, 'a': a,'b':b, 'c':c})

    else:
        form = Income_answerForm()
    return render(request,  'ranq/test_income.html',{'q':q, 'form': form})

#20190905 소득/연봉 달성 달성가능성
def goal_income(request):
    if request.method == "POST":
        form = Goal_IncomeForm(request.POST)
        if form.is_valid():
            ans = form.save(commit=False)
            cur_income = ans.cur_income
            goal_income = ans.goal_income
            period = ans.period
            inv_time = ans.time_1 + ans.time_2 + ans.time_3 + ans.time_4 + ans.time_5 + ans.time_6
            # inv_time = np.nan_to_num(ans.time_1) + np.nan_to_num(ans.time_2) + np.nan_to_num(ans.time_3) + np.nan_to_num(ans.time_4) + np.nan_to_num(ans.time_5) + np.nan_to_num(ans.time_6)
            prob = prob_go_income(cur_income, goal_income, period, inv_time) * 100.0
            prob = np.round_(prob,1)
            ans.save()
            ## 결과 페이지로 가는 것으로 수정해야함 2019.08.07 수정
            # return redirect('question_list') #, pk=post.pk)
            return render(request,  'ranq/goal_prob_result.html',{'ans':ans, 'prob':prob})

    else:
        form = Goal_IncomeForm()
    return render(request,  'ranq/goal_income.html',{'form': form})

def test_endure(request):
    if request.method == "POST":
        form = Endure_TestForm(request.POST)
        if form.is_valid():
            ans = form.save(commit=False)
            # period = ans.period  #카피본
            ans1 = ans.e_time
            ans.save()
            ## 결과 페이지로 가는 것으로 수정해야함 2019.08.07 수정
            # return redirect('question_list') #, pk=post.pk)
            return render(request, 'ranq/test_endure_result.html',{'ans1':ans1})

    else:
        form = Endure_TestForm()
    return render(request,'ranq/test_endure.html',{'form': form})

def test_iq(request):
    pk01 = 1
    pk02 = 2
    pk03 = 3
    pk04 = 4
    pk05 = 5
    pk06 = 6
    pk07 = 7
    pk08 = 8
    pk09 = 9
    pk10 = 10
    q01 = get_object_or_404(Iq_Questions, pk=pk01)
    q02 = get_object_or_404(Iq_Questions, pk=pk02)
    q03 = get_object_or_404(Iq_Questions, pk=pk03)
    q04 = get_object_or_404(Iq_Questions, pk=pk04)
    q05 = get_object_or_404(Iq_Questions, pk=pk05)
    q06 = get_object_or_404(Iq_Questions, pk=pk06)
    q07 = get_object_or_404(Iq_Questions, pk=pk07)
    q08 = get_object_or_404(Iq_Questions, pk=pk08)
    q09 = get_object_or_404(Iq_Questions, pk=pk09)
    q10 = get_object_or_404(Iq_Questions, pk=pk10)
    # c = q.id
    # post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = Iq_AnswersForm(request.POST)
        if form.is_valid():
            ans = form.save(commit=False)
            ans.question_01 = q01.q_num
            ans.question_02 = q02.q_num
            ans.question_03 = q03.q_num
            ans.question_04 = q04.q_num
            ans.question_05 = q05.q_num
            ans.question_06 = q06.q_num
            ans.question_07 = q07.q_num
            ans.question_08 = q08.q_num
            ans.question_09 = q09.q_num
            ans.question_10 = q10.q_num
            # ans.question_id = c
            a = ans
            ans.save()
            return render(request, 'ranq/test_iq_result.html',{'a': a})

    else:
        form = Iq_AnswersForm()
    return render(request,'ranq/test_iq.html',{'q01':q01, 'q02':q02, 'q03':q03, 'q04':q04, 'q05':q05, 'q06':q06, 'q07':q07, 'q08':q08, 'q09':q09, 'q10':q10, 'form': form})
