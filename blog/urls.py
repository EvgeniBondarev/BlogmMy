from django.urls import path
from . import views


urlpatterns = [
    path('', views.PostView.as_view()),
    path('<int:pk>/', views.PostDetale.as_view()),
    path('review/<int:pk>/', views.AddComents.as_view(), name='add_comment')
]