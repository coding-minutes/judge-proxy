from django.urls import path

from api.views.language import ListLanguageView
from api.views.judge import JudgeSubmissionView


urlpatterns = [
    path("languages", ListLanguageView.as_view()),
    path("run", JudgeSubmissionView.as_view()),
]
