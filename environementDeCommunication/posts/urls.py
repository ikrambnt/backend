# posts/urls.py
# posts/urls.py
from django.urls import path
from .views import  post_list, post_detail, post_create, post_edit, post_delete , comment_delete

app_name = 'posts'

urlpatterns = [
    path('list/', post_list, name='post_list'),
    path('<int:pk>/', post_detail, name='post_detail'),
    path('create/', post_create, name='post_create'),
    path('<int:pk>/edit/', post_edit, name='post_edit'),
    path('<int:pk>/delete/', post_delete, name='post_delete'),
    path('<int:pk>/', post_detail, name='post_detail'),
    path('<int:pk>/comment/delete/', comment_delete, name='comment_delete')
]
