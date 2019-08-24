from django import forms
from .models import Question, Short_answer, U_Info_Income
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
