from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from user.models import Users
from .serializers import UsersSerializer
from .email_sending import *


# class UserView(generics.ListCreateAPIView):
#     queryset = Users.objects.all()
#     serializer_class = UsersSerializer
#
#     # for i in queryset:
#     #     send_data(i.email, i.city, i.name_of_receiver)


class UserView(APIView):
    """Class based view to get all the object's details and to post data."""

    def get(self, request):
        movies = Users.objects.all()
        serializer = UsersSerializer(movies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UsersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            send_data(serializer.data['email'], serializer.data['city'], serializer.data['name_of_receiver'])
            return Response(serializer.data)
        else:
            """If you write status=status.HTTP_400_BAD_REQUEST then it will not show
            the exception raised by the validator, in place of that it will show 400 
            Bad Request.
            But if you write serializer.errors then it will show the exception raised
            by the validators."""
            return Response(serializer.errors)
