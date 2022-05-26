from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RegisterUserSerializer, UpdateUserSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import generics 
from users.models import NewUser
from rest_framework.parsers import MultiPartParser, FormParser

class CustomUserCreate(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        reg_serializer = RegisterUserSerializer(data=request.data)
        if reg_serializer.is_valid():
            newuser = reg_serializer.save()
            if newuser:
                return Response(status=status.HTTP_201_CREATED)
        return Response(reg_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Username(generics.ListAPIView):
    queryset = NewUser.objects.all()
    serializer_class = RegisterUserSerializer
    def get_queryset(self):
        user = self.request.user
        username = NewUser.objects.filter(user_name=user)
        return username


class BlacklistTokenView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        try:
            refresh_token = request.data['refresh_token']
            token = RefreshToken(refresh_token)
            token.blacklist()
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class UserProfileUpload(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def patch(self, request, format=None):
        print(request.data)
        serializer = RegisterUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UpdateUser(generics.RetrieveUpdateAPIView):
    queryset = NewUser.objects.all()
    serializer_class = UpdateUserSerializer
    def get_queryset(self):
        #This works with id
        id = self.kwargs['pk']
        username = NewUser.objects.filter(id=id)
        return username
        #This works as user logged in only!
        # user = self.request.user
        # username = NewUser.objects.filter(user_name=user)
        # return username
