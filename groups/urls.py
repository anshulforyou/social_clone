from django.urls import path, include
from . import views

app_name = 'groups'

urlpatterns = [
    path('', views.ListGroups.as_view(), name = 'all'),
    path('new/', views.CreateGroup.as_view(), name='create'),
    path('posts/in/<str:slug>', views.SingleGroup.as_view(),name = 'single'),
    path('join/<str:slug>', views.JoinGroup.as_view(), name='join'),
    path('leave/<str:slug>', views.LeaveGroup.as_view(), name='leave'),

]