from django import forms
from .models import Question, Short_answer, U_Info_Income, Goal_Income, Endure_Test, Iq_Questions, Iq_Answers
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

class Endure_TestForm(forms.ModelForm):
    class Meta:
        model = Endure_Test
        fields = ('e_time',)

class Iq_QuestionsForm(forms.ModelForm):
    class Meta:
        model = Iq_Questions
        fields = ('q_num',	'q_img_url',	'q_desc',	'q_ans',	'q_score')

class Iq_AnswersForm(forms.ModelForm):
    class Meta:
        model = Iq_Answers
        fields = ('user_id',	'score',	'answer_01',	'answer_02',	'answer_03',	'answer_04',	'answer_05',	'answer_06',	'answer_07',	'answer_08',	'answer_09',	'answer_10')
