from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status  #List of handy HTTP status codes
from rest_framework import viewsets

from . import serializers


# APIView -> parent class from django_rest
# We have to define all the url with HTTP methos
class HelloApiView(APIView):
    """Test API View"""

    #used in  POST / PATCH request
    serializer_class = serializers.HelloSerializer 

    def get(self, request, format=None):
        """Returns a list of APIView features"""

        # The format=None is to define a format suffix at the end of the end point url

        an_apiview = [
            'uses HTTP methods as funciton (get, post, patch, put, delete)',
            'is similar to a traditional Django View',
            'Gives you the most control ovet=r the application logic',
            'Is mapped manually to URLs',
        ]

        #respnose should contain either Dict or List, the frontend will expect a json format response so either dict or list
        return Response({
            'message': 'Hello!',
            'an_apiview': an_apiview,
        })

    def post(self, request):
        """Hellw message with out name"""

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():

            name = serializer.validated_data.get('name')
            # email = serializer.validated_data.get('email')
            message = f'Hello, {name}'    
            return Response({
                'message': message
            })

        else:
            return Response(
                serializer.errors, 
                status=status.HTTP_400_BAD_REQUEST
                )


    def put(self, request, pk=None):  #pk is the id of the object that we are updating
        """Handle updating objects"""
        return Response({
            'method': 'PUT'
        })

    def patch(self, request, pk=None):
        """Handles a patial update of an object"""
        return Response({
            'method': 'PATCH'
        })

    def delete(self, request, pk=None):
        """Delete an object"""

        return Response({
            'method': 'DELETE'
        }) 



class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet """

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a hello message"""

        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLs using Routers',
            'Provides more functionality with less code',
        ]

        return Response({
            'message': 'Hello',
            'a_viewset': a_viewset,
        })


    def create(self, request):
        """Create a new hello message"""

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():

            name = serializer.validated_data.get('name')
            message = f'Hello, {name}'

            return Response({
                'message': message
            })
        else:

            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""
        return Response({
            'http_method': 'GET'
        })

    def update(self, request, pk=None):
        """Updating an object"""
        return Response({
            'http_method': 'PUT'
        })

    def partial_update(self, request, pk=None):
        """Hanlde updatin part of an object"""

        return Response({
            'http_method': 'PATCH'
        })

    def destroy(self, request, pk=None):
        """Removing an object"""

        return Response({
            'http_method': 'DELETE'
        })