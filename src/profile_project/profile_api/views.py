from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import models

from . import serializers
# Create your views here.

class HelloApiView(APIView):
    """Test APIView. """

    serializer_class = serializers.HelloSerialzer

    def get(self, request, format=None):
        """Return a list of APIView features."""

        an_apiview = [
        'Uses HTTP methods as function (get, post, patch, put , delete)',
        'It is similar to a traditional Django View',
        'Gives you the most control over your logic',
        'Is mapped manaully to URLs'
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        """create a hello message with our name"""

        serializer = serializers.HelloSerialzer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handles updating objects"""
        return Response({'method': 'put'})

    def patch(self, request, pk=None):
        """patch request, only updates fields provided in request"""
        return Response({'method' : 'patch'})

    def delete(self, request, pk=None):
        """deletes an object"""
        return Response({'method' : 'delete'})

class HelloViewSet(viewsets.ViewSet):
    """Test ViewSet"""
    serializer_class = serializers.HelloSerialzer

    def list(self, request):
        """Return Hello message"""

        a_viewset = [
        'Uses actions like list, create, retrieve, update, partial_update',
        'Automatically maps to URLs using Routers',
        'Provides more functionality with less code'
        ]

        return Response({'message': 'Hello', 'a_viewset': a_viewset})

    def create(self, request):
        """create a hello message"""

        serializer = serializers.HelloSerialzer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message' : message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Handles getting object by id. """

        return Response({'http_method' : 'GET'})

    def update(self, request, pk=None):
        """Handles updating an object"""

        return Response({'http_method' : 'PUT'})

    def partial_update(self, request, pk=None):
        """Handles updating a part of an object. """

        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handles removing an object"""

        return Response({'http_method': 'DELETE'})

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating profiles."""

    serializer_class = serializers.UserProfileSerializer

    queryset = models.UserProfile.objects.all()
