from django.urls import path

from api.views.language import ListLanguageView


urlpatterns = [
    path("languages", ListLanguageView.as_view())
]
