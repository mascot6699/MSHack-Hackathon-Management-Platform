
from . import models, serializers

from datetime import datetime, timedelta
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions



class Process(APIView):
    """
    These apis are for general purpose
    """

    def get(self, request, format=None):
        """
        GET api for getting particular template from id
        """
        parsed_content = request.query_params.get("Body").split(' ')
        body = " ".join(parsed_content[1:])
        return Response(body, status=status.HTTP_200_OK, content_type="text/plain")


