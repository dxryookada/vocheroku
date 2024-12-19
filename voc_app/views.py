from django.shortcuts import render
from django.views.generic import TemplateView

class PublishView(TemplateView):
  template_name = "survey/publish.html"

class QrView(TemplateView):
  template_name = "survey/qr.html"

  def post(self, request, *args, **kwargs):
     # POSTリクエストが送信されたときに処理を行いたい場合はここで行います。
     # 必要な処理を追加してください。 
     return self.get(request, *args, **kwargs)

class SurveyView(TemplateView):
  template_name = "survey/survey.html"

class ComView(TemplateView):
  template_name = "survey/complete.html"

  def post(self, request, *args, **kwargs):
    # POSTリクエストが送信されたときに処理を行いたい場合はここで行います。
    # 必要な処理を追加してください。 
    return self.get(request, *args, **kwargs)
