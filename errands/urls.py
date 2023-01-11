from django.urls import path
from . import views

urlpatterns =[
    path('',views.index, name='home'),
    path('create/', views.create_errands, name='create-errands'),
    path('errands/<id>/', views.errands_detail, name='errands'),
    path('errands-delete/<id>/', views.errands_delete, name='errands-delete'),
    path('edit-errands/<id>/', views.errands_edit, name='errands-edit'),
]
