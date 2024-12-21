from django.shortcuts import render
from django.views.generic import TemplateView

# --- ログインページ
class LoginView(TemplateView):
  template_name = "login.html"

# --- 一般従業員ページ
class GeneralView(TemplateView):
  template_name = "general/general.html"

class UpdateView(TemplateView):
  template_name = "general/update.html"

# --- 管理者ページ
class AdminView(TemplateView):
  template_name = "admin/admin.html"