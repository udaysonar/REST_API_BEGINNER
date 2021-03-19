from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class HelloAPIView(APIView):
    """Test API View"""

    def get(self,request,format=None):
        """Return a list of APIView Features"""
        an_apiview=[
            'Uses HTTP methods as function(get,post,put,patch,delete)',
        ]

        return Response({'message':'Hello','an_apiview':an_apiview})