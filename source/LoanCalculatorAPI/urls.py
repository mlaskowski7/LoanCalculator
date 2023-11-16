from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name= "index"),
    path('loan/<str:loan_title>',views.LoanDescription, name="loan_description")
]