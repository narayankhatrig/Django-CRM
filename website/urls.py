from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    #path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('userInfo/<int:pk>', views.getUserInformation, name='userInfo'),
    path('delete_user/<int:pk>', views.deleteUserInformation, name='delete'),
    path('add_user/>', views.addUserInformation, name='add'),
]