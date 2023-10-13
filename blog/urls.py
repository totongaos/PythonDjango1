from django.urls import path
from . import views

urlpatterns = [
  path('', views.list, name = 'blog'),
  path('<int:id>/', views.post, name='post'),
  #ở PostDetailView thì class sẽ truy vấn bằng primary key, nên thay url id thành pk để path hợp lệ.
  # path('<int:pk>/', views.post, name='post'), #blog/id
]

