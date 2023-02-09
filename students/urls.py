from django.urls import path

from . import views

urlpatterns = [
    path('', views.StudentListAPIView.as_view()),
    path('<int:pk>/', views.StudentDetailAPIView.as_view())
]