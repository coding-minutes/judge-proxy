from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers

from api.serializers.base import BaseSerializer
from judge_proxy.config import Config


class LanguageSerializer(BaseSerializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    editor_code = serializers.CharField()


class ListLanguageView(APIView):
    def get(self, request) -> Response:
        languages = Config.LANGUAGES
        serializer = LanguageSerializer(languages, many=True)

        return Response(serializer.data)
