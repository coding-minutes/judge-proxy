from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response

from api.exapi.judge0.service import get_judge0_exapi


class SubmissionDeserializer(serializers.Serializer):
    source_code = serializers.CharField()
    language_id = serializers.IntegerField()
    stdin = serializers.CharField()

class JudgeSubmissionView(APIView):
    parser_classes = [JSONParser]

    def post(self, request):
        submission = SubmissionDeserializer(data=request.data)
        submission.is_valid(raise_exception=True)
        submission = submission.validated_data

        token = get_judge0_exapi().create_submission(
            source_code=submission.get("source_code"),
            language_id=submission.get("language_id"),
            stdin=submission.get("stdin"),
        )

        return Response({
            "submission_id": token
        })
