"""Module that contains all the views that will be used in this project
"""
from django.shortcuts import render
# from django.http import JsonResponse

from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import Users_serializer, Orders_serializer
from .models import Users, Orders

# Create your views here.

class Users_viewset(viewsets.ViewSet):
    """Class that will handle views for the User model
    """
    
    def all_users(self, request):
        """Returns a list of all the Users registred in alphabetical order (by name and last name).
        """
        queryset = Users.objects.all().order_by('name', 'last_name')
        serializer = Users_serializer(queryset, many=True)

        return Response(serializer.data)

    def user_id(self, request, user_id):
        """Returns the info about a user depending on the ID passed
        """
        queryset = Users.objects.filter(user_id=user_id)
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


class Orders_viewset(viewsets.ViewSet):
    """Class that will handle views for the Order model
    """
    
    def order_id(self, request, order_id):
        """Returns the information about an order depending on the ID passed
        """
        queryset = Orders.objects.filter(order_id=order_id)
        serializer = Orders_serializer(queryset, many=True)

        return Response(serializer.data)

    def new_order(self, request):
        """Creates a new user if the data sent in POST is valid.
        If the data is not valid will return a 400 BAD REQUEST error.
        """
        serializer = Orders_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def order_arg(self, request, arg):
        """Return information about orders depending on the information passed
        Can handle:
            - Multiple order_id: Separated by comma -> '1,2,7,9'
            - Dates: Two dates to get order_id of the orders between those dates YYYY-MM-DD-YYYY-MM-DD -> '2020-04-07-2021-04-07'
        """
        if arg.find("-") != -1:
            date_start = arg[0:10]
            date_end = arg[11:21]

            queryset = Orders.objects.filter(date__range=(date_start, date_end))
            serializer = Orders_serializer(queryset, many=True)
        else:
            ids = arg.split(",")
            queryset = Orders.objects.filter(order_id__in=ids)
            serializer = Orders_serializer(queryset, many=True)
        return Response(serializer.data)

    def order_by_user(self, request, user_id):
        """Returns the information about an order depending on the ID passed
        """
        queryset = Orders.objects.filter(user=user_id)
        serializer = Orders_serializer(queryset, many=True)

        return Response(serializer.data)