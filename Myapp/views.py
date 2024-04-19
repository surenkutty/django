# myapp/views.py
from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from .Serializers import UserSerializer
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login


class SignupView(CreateAPIView, ListAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
    def post(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        if response.status_code == status.HTTP_201_CREATED:
            user = response.data
            token, _ = Token.objects.get_or_create(user_id=user['id'])
            response.data['token'] = token.key
            print(token)
            
        return Response({
            'token': str(token),
            'username':user.username,
        })
    
class DbViews(ListAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)
    
    
class LoginViews(APIView):
    def post(self,request):
        username=request.data.get('username')
        password=request.data.get('password')
        user=authenticate(request,username=username,password=password)
    
        if not username or not password:
            return Response({
                "error":'username and password are required'
            },status=status.HTTP_400_BAD_REQUEST)

        
        if user is not None:
            login(request,user)
            return Response({
                'message':'loginSucessFully'
                
                },status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
