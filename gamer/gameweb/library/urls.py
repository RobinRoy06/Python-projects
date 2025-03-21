from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name="index"),
    path("delete/<int:game_id>/", views.delete_game, name="delete_game"),
    path("update/<str:pk>/", views.update_game, name="update_game"),
    path("view/<str:pk>/", views.view_game, name="view_game"),
    

]