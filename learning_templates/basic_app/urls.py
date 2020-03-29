from django.urls import path
from basic_app import views

# Template tagging, namespace
app_name = 'basic_app' # always app_name set to your application's name

urlpatterns = [
    path('relative/', views.relative, name='relative'),
    path('other/', views.other, name='other'),
]
