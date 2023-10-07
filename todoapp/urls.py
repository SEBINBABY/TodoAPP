from django.urls import path
from .import views
urlpatterns = [
    path('',views.home,name="home"),
    path('login/',views.Login,name="login"),
    path('signup/',views.signup,name="signup"),
    path('Logout/',views.Logout,name="Logout"),
    path('add_todo/',views.add_todo,name="add_todo"),
    path('delete_todo/<int:id>',views.delete_todo,name="delete_todo"),
    path('update_todo/<int:id>/<str:status>',views.update_todo,name="update_todo"),
]