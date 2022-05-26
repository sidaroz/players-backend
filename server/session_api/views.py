from email import message
from rest_framework import generics 
from sesh.models import Post
from .serializers import PostSerializer, UpdateSerializer
from rest_framework.permissions import SAFE_METHODS, BasePermission, IsAdminUser, DjangoModelPermissionsOrAnonReadOnly, IsAuthenticated, AllowAny
from rest_framework import viewsets
from rest_framework import filters
from django.shortcuts import get_object_or_404, render
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
import django_filters

from session_api import serializers

class PostUserWritePermission(BasePermission):
    message = 'Editing posts is restricted to the creator of this session.'

    def has_object_permission(self, request, view, obj):
        
        if request.method in SAFE_METHODS:
            return True

        return obj.player == request.user

class PostList(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = PostSerializer

    def get_queryset(self):
        user = self.request.user
        return Post.objects.all()

class PostDetail(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer

    # def get_queryset(self):
    #     id = self.request.query_params.get('id', None)
    #     print(id)
    #     return Post.objects.filter(id=id)
    def get_queryset(self):
        id = self.kwargs['pk']
        print(id)
        return Post.objects.filter(id=id)

# class PostDelete(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = [PostUserWritePermission]
#     serializer_class = PostSerializer
#     def get_queryset(self):
#         id = self.kwargs['pk']
#         print(id)
#         return Post.objects.delete(id=id)

class PostListDetailfilter(generics.ListAPIView):
   queryset = Post.objects.all()
   serializer_class = PostSerializer
   filter_backends = [filters.SearchFilter]
   search_fields = ['^area', '=difficulty']

#POST
class CreatePost(generics.CreateAPIView):
    permission_classes = [AllowAny]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class EditPost(generics.RetrieveUpdateAPIView):
    class Meta:
        fields = ['players_needed']
    permission_classes = [IsAuthenticated]
    serializer_class = UpdateSerializer
    queryset = Post.objects.all()


class DeletePost(generics.RetrieveDestroyAPIView):
    permission_classes = [AllowAny]
    serializer_class = PostSerializer
    def get_queryset(self):
        id = self.kwargs['pk']
        print(id)
        return Post.objects.filter(id=id)


# THIS WORKS
# class PostList(viewsets.ModelViewSet):
#     permission_classes = [PostUserWritePermission]
#     serializer_class = PostSerializer

#     def get_object(self, queryset=None, **kwargs):
#         item = self.kwargs.get('pk')
#         #CHANGE id=item to any other parameter you would want to search for
#         return get_object_or_404(Post, id=item)

#     def get_queryset(self):
#         return Post.objects.all()


# class PostList(viewsets.ViewSet):
#     permission_classes = [IsAuthenticated]
#     queryset = Post.objects.all()

#     def list(self, request):
#         serializer_class = PostSerializer(self.queryset, many=True)
#         return Response(serializer_class.data)

#     def retrieve(self, request, pk=None):
#         post = get_object_or_404(self.queryset, pk=pk)
#         serializer_class = PostSerializer(post)
#         return Response(serializer_class.data)

# THIS WORKS AS INTENDED IF NOTHING ELSE WORKS
# class PostList(generics.ListCreateAPIView):
#     permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
    

# class PostDetail(generics.RetrieveUpdateDestroyAPIView, PostUserWritePermission):
#     permission_classes = [PostUserWritePermission]
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
   