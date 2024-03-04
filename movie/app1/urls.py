from django.urls import path
from app1 import views
app_name='app1'

urlpatterns = [
    #path('',views.home,name="home"),
    path('',views.MovieList.as_view(),name="home"),
    #path('add',views.add,name="add"),

    path('add/',views.Movieadd.as_view(),name="add"),

    #path('details/<int:p>', views.details, name="details"),
    path('movie/<int:pk>',views.MovieDetail.as_view(),name="details"),

    #path('edit/<int:p>',views.edit,name="edit"),
    path('edit/<int:pk>/',views.Movieupdate.as_view(),name="edit"),

    #path('delete/<int:p>', views.delete, name="delete"),
    path('delete/<int:pk>/', views.Moviedelete.as_view(), name="delete"),

]
