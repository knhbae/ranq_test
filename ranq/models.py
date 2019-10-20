from django.db import models
from django.utils import timezone
from django import forms
from datetime import datetime, timedelta, date
####################Cola#################################

class Question(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField(null=True)
    image = models.ImageField(upload_to='', blank=True)
    # answer = models.CharField(max_length=100)
    ques = models.TextField(null=True)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class Short_answer(models.Model):
    question = models.ForeignKey('ranq.Question', on_delete=models.CASCADE)
    answer = models.CharField(max_length=100)
    output = models.CharField(max_length=100)
    #ArrayField(models.CharField(max_length=10, blank=True), size=10))
    def __str__(self):
        return self.title

#목표 연봉과 노력할 것 들
class Goal_Income(models.Model):
    cur_income = models.FloatField()
    goal_income = models.FloatField()
    period = models.FloatField()
    plan_1 = models.CharField(max_length=30, null=True, blank=True)
    time_1 = models.FloatField(null=True, blank=True,default=0)
    plan_2 = models.CharField(max_length=30, null=True, blank=True)
    time_2 = models.FloatField(null=True, blank=True,default=0)
    plan_3 = models.CharField(max_length=30, null=True, blank=True)
    time_3 = models.FloatField(null=True, blank=True,default=0)
    plan_4 = models.CharField(max_length=30, null=True, blank=True)
    time_4 = models.FloatField(null=True, blank=True,default=0)
    plan_5 = models.CharField(max_length=30, null=True, blank=True)
    time_5 = models.FloatField(null=True, blank=True,default=0)
    plan_6 = models.CharField(max_length=30, null=True, blank=True)
    time_6 = models.FloatField(null=True, blank=True,default=0)
    created_date = models.DateTimeField(default=timezone.now)
    ip = models.CharField(max_length=15, default=None, null=True)  # ip 주소

class U_Info_Income(models.Model):
    y_income	=	models.FloatField()
    rank_income = models.FloatField(null=True, blank=True)
    m_income	=	models.FloatField(null=True, blank=True)
    de_income	=	models.FloatField(null=True, blank=True)
    de_amount	=	models.FloatField(null=True, blank=True)
    na_pension	=	models.FloatField(null=True, blank=True)
    he_insurance	=	models.FloatField(null=True, blank=True)
    a_insurance	=	models.FloatField(null=True, blank=True)
    em_insurance	=	models.FloatField(null=True, blank=True)
    in_tax	=	models.FloatField(null=True, blank=True)
    resi_tax	=	models.FloatField(null=True, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    ip = models.CharField(max_length=15, default=None, null=True)  # ip 주소
#for U_Info_Income
class Info_Income(models.Model):
    y_income	=	models.FloatField()
    m_income	=	models.FloatField(null=True, blank=True)
    de_income	=	models.FloatField(null=True, blank=True)
    de_amount	=	models.FloatField(null=True, blank=True)
    na_pension	=	models.FloatField(null=True, blank=True)
    he_insurance	=	models.FloatField(null=True, blank=True)
    a_insurance	=	models.FloatField(null=True, blank=True)
    em_insurance	=	models.FloatField(null=True, blank=True)
    in_tax	=	models.FloatField(null=True, blank=True)
    resi_tax	=	models.FloatField(null=True, blank=True)

#for U_Info_Income
class Rank_Income(models.Model):
    y_income = models.FloatField()
    rank = models.FloatField()
    created_date = models.DateTimeField(default=timezone.now)
#for 참을성 TEST
class Endure_Test(models.Model):
    e_time = models.FloatField()
    created_date = models.DateTimeField(default=timezone.now)
    ip = models.CharField(max_length=15, default=None, null=True)  # ip 주소

class Iq_Questions(models.Model):
    q_num	=	models.CharField(max_length=50)
    q_img_url	=	models.CharField(max_length=200)
    q_desc	=	models.CharField(max_length=1000)
    q_ans	=	models.CharField(max_length=50)
    q_score	=	models.FloatField()

class Iq_Answers(models.Model):
    user_id = models.CharField(max_length=50)
    score	=	models.FloatField()
    question_01	=	models.CharField(max_length=50)
    question_02	=	models.CharField(max_length=50)
    question_03	=	models.CharField(max_length=50)
    question_04	=	models.CharField(max_length=50)
    question_05	=	models.CharField(max_length=50)
    question_06	=	models.CharField(max_length=50)
    question_07	=	models.CharField(max_length=50)
    question_08	=	models.CharField(max_length=50)
    question_09	=	models.CharField(max_length=50)
    question_10	=	models.CharField(max_length=50)
    answer_01	=	models.CharField(max_length=50)
    answer_02	=	models.CharField(max_length=50)
    answer_03	=	models.CharField(max_length=50)
    answer_04	=	models.CharField(max_length=50)
    answer_05	=	models.CharField(max_length=50)
    answer_06	=	models.CharField(max_length=50)
    answer_07	=	models.CharField(max_length=50)
    answer_08	=	models.CharField(max_length=50)
    answer_09	=	models.CharField(max_length=50)
    answer_10	=	models.CharField(max_length=50)
    created_date = models.DateTimeField(default=timezone.now)
    ip = models.CharField(max_length=15, default=None, null=True)  # ip 주소
