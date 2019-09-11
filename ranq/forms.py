from django import forms
from .models import Question, Short_answer, U_Info_Income, Goal_Income
from django.forms.models import ModelForm

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('title', 'desc', 'image','ques')

class Short_answerForm(forms.ModelForm):
    class Meta:
        model = Short_answer
        fields = ('answer',)

class Income_answerForm(forms.ModelForm):
    class Meta:
        model = U_Info_Income
        fields = ('y_income',)

class Goal_IncomeForm(forms.ModelForm):
    class Meta:
        model = Goal_Income
        fields = ('cur_income','goal_income','period',
                  'plan_1','time_1',
                  'plan_2','time_2',
                  'plan_3','time_3',
                  'plan_4','time_4',
                  'plan_5','time_5',
                  'plan_6','time_6')
