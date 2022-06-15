from django.urls import path
from .views import login, signup

app_name = 'account'

urlpatterns = [
    path('signup/', signup, name='signupview'),
    path('login/', login, name='loginview'),
]