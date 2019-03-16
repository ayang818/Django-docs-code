from django.contrib import admin
from django.urls import path,include
from . import views

# polls/
#参数前不能随便加空格
#所有路由后都要加/
#最简单的方法就是把他们放入各自的 命名空间 中，也就是把这些模板放入一个和 自身 应用重名的子文件夹里
app_name = 'polls'

# 多用name代替硬编码的url
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
]   