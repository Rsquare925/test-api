from django.contrib import admin
from django.urls import path, include
from .views import *
 
urlpatterns = [
    path('user/', UserAPI.as_view()),
    path('register-user/', RegisterUser.as_view())
    # path('', home),
    # path('signup/', signup),
    # path('update-user/<id>/', update_user),
    # path('delete-user/<id>/', delete_user)

]