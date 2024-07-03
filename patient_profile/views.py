from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import UserSerializer
from .models import CustomUser
import jwt, datetime
from rest_framework.views import APIView

# Create your views here.
class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']
        print(email)
        print(password)
        user = CustomUser.objects.filter(email=email).first()

        if user is None:
            return Response({'message': 'User not found'}, status=status.HTTP_400_BAD_REQUEST)
        
        if not user.check_password(password):
            return Response({'message': 'Incorrect password'}, status=status.HTTP_400_BAD_REQUEST)

        payload = {
            'id': user.id,
            'name': user.name,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=600),
            'iat': datetime.datetime.utcnow()
        }
        
        token = jwt.encode(payload, 'secret', algorithm='HS256')

        # return Response({'jwt': token})
        response = Response()
        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
                'id': user.id,
                'name': user.name,
                'jwt': token
            }   
        return response