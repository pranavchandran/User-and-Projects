from django.urls import path
from . import views

app_name = 'projects'

urlpatterns = [
    path('',views.IndexClassView.as_view(),name='index'),
    path('<int:pk>/',views.ProjectDetail.as_view(),name='detail'),
    path('add/', views.CreateProject.as_view(),name='create_item'),
    path('view/', views.view_item,name='view_item'),
    path('update/<int:id>/', views.update_item, name='update_item'),
    path('delete/<int:id>', views.delete_item, name='delete_item'),
]