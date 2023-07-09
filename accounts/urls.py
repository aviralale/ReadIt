from django.urls import path
from accounts.views import *

app_name = 'accounts'

urlpatterns = [
    # API TO COMMENT
    path('<str:username>/',account,name='account'),
]