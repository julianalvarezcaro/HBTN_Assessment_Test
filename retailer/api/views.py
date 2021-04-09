"""Module that contains all the views that will be used in this project
"""
from django.shortcuts import render
# from django.http import JsonResponse

from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import Users_serializer
from .models import Users

# Create your views here.

class Users_viewset(viewsets.ViewSet):
    """
    OrdersViewSet is the class that will handle views for the Order model
    """
    
    def all_users(self, request):
        """Returns a list of all the Users registred in alphabetical order (by name and last name).
        """
        queryset = Users.objects.all().order_by('name', 'last_name')
        serializer = Users_serializer(queryset, many=True)

        return Response(serializer.data)
    
    def new_user(self, request):
        """Creates a new user if the data sent in POST is valid.
        If the data is not valid will return a 400 BAD REQUEST error.
        """
        serializer = Users_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    # def get_order(self, request, id=None):
    #     """Will retrieve an order with the given ID.
    #     """
    #     queryset = Orders.objects.all()
    #     serializer = OrdersSerializer(queryset, many=True)

    #     return Response(serializer.data)

        
    #     # message = f'You submitted ID: {id}'
    #     # return HttpResponse(serialized)