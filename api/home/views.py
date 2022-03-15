from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
# Create your views here.

class RegisterUser(APIView):

    def post(self, request):
        serializer = UserSerializer(data = request.data)

        if not serializer.is_valid():
            return Response({'status': 403, 'error': serializer.errors, 'message': 'something went wrong'})

        serializer.save()

        user = User.objects.get(username=serializer.data['username'])
        refresh = RefreshToken.for_user(user)

        return Response({'status': 200, 
                            'payload': serializer.data, 
                            'message': 'New User Created',
                            'refresh': str(refresh),
                            'access': str(refresh.access_token),
                        })

class UserAPI(APIView):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        user_objs = User1.objects.all()
        serializer = User1Serializer(user_objs, many=True)

        return Response({'status': 200, 
                            'payload': serializer.data,
                        })

    # def post(self, request):
    #     serializer = User1Serializer(data = request.data)

    #     if not serializer.is_valid():
    #         return Response({'status': 403, 'error': serializer.errors, 'message': 'something went wrong'})

    #     serializer.save()
    #     return Response({'status': 200, 'payload': serializer.data,         'message': 'you sent' })

    def put(self, request):
        pass

    def patch(self, request):
        try:
            user_obj = User1.objects.get(id = request.data['id'])

            serializer = User1Serializer(user_obj, data=request.data, partial=True)
            if not serializer.is_valid():
                return Response({'status': 403, 'error': serializer.errors, 'message': 'something went wrong'})
            
            serializer.save()
            return Response({'status': 200, 'payload': serializer.data, 'message': 'data updated'})
        except Exception as e:
            return Response({'status': 403, 'message': 'invalid id'})


    def delete(self, request):
        try:
            id = request.GET.get('id')
            user_obj = User1.objects.get(id = id)
            user_obj.delete()
            return Response({'status': 200, 'message': 'user deleted'})

        except Exception as e:
            print(e)
            return Response({'status': 403, 'message': 'invalid id'})
        


# @api_view(['GET'])
# def home(request):
#     user_objs = User.objects.all()
#     serializer = UserSerializer(user_objs, many=True)

#     return Response({'status': 200, 
#                         'payload': serializer.data
#                     })

# @api_view(['POST'])
# def signup(request):
#     serializer = UserSerializer(data = request.data)

#     if not serializer.is_valid():
#         return Response({'status': 403, 'error': serializer.errors, 'message': 'something went wrong'})

#     serializer.save()
#     return Response({'status': 200, 'payload': serializer.data, 'message': 'you sent'})


# @api_view(['PUT'])
# def update_user(request, id):
#     try:
#         user_obj = User.objects.get(id = id)

#         serializer = UserSerializer(user_obj, data=request.data, partial=True)
#         if not serializer.is_valid():
#             return Response({'status': 403, 'error': serializer.errors, 'message': 'something went wrong'})
        
#         serializer.save()
#         return Response({'status': 200, 'payload': serializer.data, 'message': 'data updated'})
#     except Exception as e:
#         return Response({'status': 403, 'message': 'invalid id'})


# @api_view(['DELETE'])
# def delete_user(request, id):
#     try:
#         user_obj = User.objects.get(id = id)
#         user_obj.delete()
#         return Response({'status': 200, 'message': 'user deleted'})

#     except Exception as e:
#         print(e)
#         return Response({'status': 403, 'message': 'invalid id'})
        