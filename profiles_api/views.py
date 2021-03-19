from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers
# Create your views here.

class HelloAPIView(APIView):
    """Test API View"""
    serializer_class=serializers.HelloSerializers

    def get(self,request,format=None):
        """Return a list of APIView Features"""
        an_apiview=[
            'Uses HTTP methods as function(get,post,put,patch,delete)',
        ]

        return Response({'message':'Hello','an_apiview':an_apiview})

    def post(self,request):
        """Create a hello message with our name"""
        serializer =self.serializer_class(data=request.data)

        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            msg=f'Hello {name}'
            return Response({'message ':msg})
        else:
            return Response(serializer.errors, 
             status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk=None):
        """Handle Updating an object"""

        return Response({'method':'PUT'})
    
    def patch(self,request,pk=None):
        """Handles a partial Updating of an object"""

        return Response({'method':'PATCH'})

    def delete(self,request,pk=None):
        """Handles a partial Updating of an object"""

        return Response({'method':'DELETE'})