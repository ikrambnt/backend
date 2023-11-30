from django.urls import path
from . import views

app_name = "groups"


urlpatterns = [
    path('group_details/<int:group_id>/', views.details_group, name='group_detail'),
    path('create_group/', views.create_group , name='create_group'),    
    path('group_list/', views.groups_list, name='group_list'), 
    path('update_group/<int:group_id>/', views.update_group, name='update_group'),
    path('delete_group/', views.delete_group, name='delete_group'),
    
]
