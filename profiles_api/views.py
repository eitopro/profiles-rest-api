from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """test"""

    def get(self, request, format=None):
        an_apiview = [
            'Uses HTTP methods as functions (get, post, patch, put, delete)',
            'Is similar to a tradditional Django View',
            'Gives you the most control over your application logic',
            'It maps manually to URLs',
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})
