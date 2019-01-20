
from . import models, serializers

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions


@method_decorator(csrf_exempt, name='dispatch')
class Scan(APIView):
    """
    These apis are for general purpose
    """
    def post(self, request, format=None):
        """
        GET api for getting particular template from id
        """
        parsed_content = request.POST.get("Body").split(' ')
        body = " ".join(parsed_content[1:])
        return Response(body, status=status.HTTP_200_OK, content_type="text/plain")


