from app.views import  home,login,signup,app_todo,signout,delete_todo,change_todo
from django.urls import path

urlpatterns = [
 
    path("",home,name="home"),
    path('login',login,name="login"),
    path('signup',signup,name="signup"),
    path("app_todo",app_todo),
    path("logout",signout),
    path("delete/<int:id>",delete_todo,name="delete"),
    path("change_status/<int:id>/<str:status>",change_todo,name="change")
]
