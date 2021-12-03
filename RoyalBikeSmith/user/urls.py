from django.urls import path, re_path
from django.contrib.auth import views as auth_views 
from . import views


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create/', views.create_job_card, name='jobcard'),
    path('list/',views.listJobCard,name="listJobCard" ),
    path('detail/<int:id>', views.detailView, name="detail")

]