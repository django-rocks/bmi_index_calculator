from django.urls import path
from . import views

urlpatterns = [
    path('', views.example_view),
    path('feedback',views.feedback_review),
#    path('',views.example_view)
]
