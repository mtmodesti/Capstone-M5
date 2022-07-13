from django.urls import path

from . import views

urlpatterns = [
   path("convenios/", views.CreateConvenioView().as_view()),
   path("convenios/delete/<pk>", views.RetrieveUpdateDestroyView().as_view()),
]
