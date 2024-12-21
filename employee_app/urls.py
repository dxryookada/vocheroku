from django.urls import path
from . import views

urlpatterns = [
  path('', views.LoginView.as_view(), name='login'),
  # --- 一般ユーザー
  path('general', views.GeneralView.as_view(), name='general'),
  path('update', views.UpdateView.as_view(), name='update'),
  # --- 管理者
  path('admin', views.AdminView.as_view(), name='admin'),
]