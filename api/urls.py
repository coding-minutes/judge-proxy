from django.urls import path

from api.views.language import ListLanguageView
from api.views.judge import JudgeSubmissionView, JudgeResultView


urlpatterns = [
    path("languages", ListLanguageView.as_view()),
    path("run", JudgeSubmissionView.as_view()),
    path("submissions/<str:token>", JudgeResultView.as_view()),
]
