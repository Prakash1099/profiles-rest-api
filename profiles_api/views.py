from rest_framework.views import APIView
from rest_framework.response import Response


# APIView -> parent class from django_rest
# We have to define all the url with HTTP methos
class HelloApiView(APIView):
    """Test API View"""

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

        



    