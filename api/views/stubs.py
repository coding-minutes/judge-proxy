from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response

from api.serializers.base import BaseSerializer
from stubs import LANGUAGE_ID_VS_STUBS


class StubSerializer(BaseSerializer):
    language_id = serializers.IntegerField()
    stub = serializers.CharField()


class ListStubsView(APIView):
    def get(self, request):
        stubs_resp = [
            {"language_id": language_id, "stub": stub}
            for language_id, stub in LANGUAGE_ID_VS_STUBS.items()
        ]

        serializer = StubSerializer(stubs_resp, many=True)
        return Response(serializer.data)
