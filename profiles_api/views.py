from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers
"""For viewsets API"""
from rest_framework import viewsets
"""End for viewsets API"""


class HelloApiView(APIView):
    """test"""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        an_apiview = [
            'Uses HTTP methods as functions (get, post, patch, put, delete)',
            'Is similar to a tradditional Django View',
            'Gives you the most control over your application logic',
            'It maps manually to URLs',
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})

    def post(self, request):
        """Create a hello message with the receivedname"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name =serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
                )
    
    def put(self, request, pk=None):
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        return Response({'method': 'PATCH'})
        
    def delete(self, request, pk=None):
        return Response({'method': 'DELETE'})
    





"""For viewsets API"""
class HelloViewSet(viewsets.ViewSet):
    serializer_class = serializers.HelloSerializer


    def list(self, request):
        a_viewset =[
            'Users actions (list, create, retrieve, update, partial_updat',
            'Automaticly maps to urls using Routers',
            'provides more functionality with less code',
        ]
        return Response({'message':'Hello!', 'a_viewset': a_viewset})
    
    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serialzer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )

    def retrieve(self, request, pk=None):
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        return Response({'http_method': 'PUT'})

    def parttial_update(self, request, pk=None):
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        return Response({'http_method': 'DELETE'})



"""End for viewsets API"""