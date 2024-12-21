from django.urls import path
from . import views

urlpatterns = [
  path('', views.PublishView.as_view(), name='publish'),
  path('qr/', views.QrView.as_view(), name='qr'),
  path('survey/', views.SurveyView.as_view(), name='survey'),
  path('complete/', views.ComView.as_view(), name='complete'),
]