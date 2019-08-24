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


class Rank_Income(models.Model):
    y_income = models.FloatField()
    rank = models.FloatField()
