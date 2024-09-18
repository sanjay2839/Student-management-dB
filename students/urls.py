from django.urls import path
from . import views

urlpatterns = [
  path('', views.login_view, name='login_view'),
  path('return_base/', views.return_base, name='return_base'),
  path('return_login/', views.return_login, name='return_login'),
  path('signup/', views.signup, name='signup'),
  path('', views.index, name='index'),
  path('<int:id>', views.view_student, name='view_student'),
  path('add/', views.add, name='add'),
  path('edit/<int:id>/', views.edit, name='edit'),
  path('delete/<int:id>/', views.delete, name='delete') ,
  path('index/', views.index, name='index'),
  path('logout/', views.logout, name='logout')
]
