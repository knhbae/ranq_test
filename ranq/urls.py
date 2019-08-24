from django.contrib import admin
from . import views
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.t_question_list, name='t_question_list'), #위의 urls.py와는 달리 include가 없습니다.
    path('t/<int:pk>/', views.t_question_detail, name='t_question_detail'),
    path('index1/', views.question_list, name='question_list'), #위의 urls.py와는 달리 include가 없습니다.
    path('q/<int:pk>/', views.question_detail, name='question_detail'),
    # path('q/<int:pk>/a_result/', views.question_a_result, name='question_a_result'),
    # path('a/<int:pk>/', views.a_detail, name='question_detail'),
    path('post/new/', views.question_new, name='question_new'),
]

urlpatterns += static(
    prefix=settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT,
)
