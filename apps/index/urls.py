from django.urls import path
from . import views
app_name = 'index'

urlpatterns =[
    path('user/register/', views.SignUpView.as_view(), name='register_user'),
    path('', views.Index.as_view(), name="index")
    
    
]