from django.urls import path
from .import views

urlpatterns =[
    path('',views.index,name='home'),
    path('',views.create_errands,name='create_errands'),
]
