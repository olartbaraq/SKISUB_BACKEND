from django.shortcuts import render
from skisub.models import BillOperation, Skisubuser
from rest_framework.views import APIView
from knox.models import AuthToken
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model, login, logout
from rest_framework.response import Response
from rest_framework import generics
from skisub.serializers import BookFlightSerializer, CarBookingSerializer, DataSerializer, RegisterSerializer, skisubUserSerializer,CabletvSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly, IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response


class RegisterView(generics.CreateAPIView):
    queryset = Skisubuser.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

class LoginView(APIView):
    permission_classes = []
    def post(self, request):
        form = AuthenticationForm(data=request.data)
        if form.is_valid():
            user = form.get_user()
            login(request, user=form.get_user())
            response = {"status_code": status.HTTP_200_OK,
                        "success": "true",
                        "message": "Successfully logged in",
                        "data": skisubUserSerializer(user).data,
                        "token": AuthToken.objects.create(user)[1]
                        }
            return Response(response)
        else:
            return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)
            



#logout
class LogoutView(APIView):
    # permission_classes = (IsAuthenticated,)

    def post(self, *args, **kwargs):
        logout(self.request)
        response = {"status_code": status.HTTP_204_NO_CONTENT,
                        "success": "true",
                        "message": "Successfully logged out",
                        "data": ""}
        return Response(response)


class BillOperationViewSet(viewsets.ModelViewSet):
    queryset = BillOperation.objects.all()

    def get_serializer_class(self):
        # Determine which serializer to use based on the request data
        if 'dataplan' in self.request.data:
            return DataSerializer
        elif 'location' in self.request.data:
            return BookFlightSerializer
        elif 'cartype' in self.request.data:
            return CarBookingSerializer
        elif 'selectbouquet' in self.request.data:
            return CabletvSerializer
        else:
            # Return a default serializer class or raise an error if needed
            # For example, you can return a generic serializer or raise an error.
            return BookFlightSerializer # You should define DefaultSerializer

    def create(self, request, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
