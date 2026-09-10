from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status  #List fo handy HTTP status codes

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
            message = f'Hello {name}'    
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