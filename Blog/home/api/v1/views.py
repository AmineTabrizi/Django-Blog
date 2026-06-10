from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.response import Response
from .serializers import *
from home.models import Post, Category
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.decorators import action
from .permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .paginations import DefaultPagination 


"""
@api_view(["GET", "Post"])
@permission_classes([IsAuthenticatedOrReadOnly])
def postList(request):
    if request.method == "GET":
        posts = Post.objects.filter(status=True)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save
        return Response(serializer.data)"""
         
'''class PostList(APIView):
    """ getting a list of posts & creating a new post """
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer

    def get(self, request):
        """ retriving a list of posts """
        posts = Post.objects.filter(status=True)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        """ Creating a post with providing data"""
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
'''

'''
class PostList(ListCreateAPIView):
    """ getting a list of posts & creating a new post """
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)'''
    
    



"""
@api_view(["GET", "PUT", "DELETE"])
def postDetail(request, id):
    
    post = Post.objects.get(pk=id, status=True)
    if request.method == "GET":
        serializer = PostSerializer(post)
        return Response(serializer.data)   
    elif request.method == "PUT":
        serializer = PostSerializer(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == "DELETE":
        post.delete()
        return Response({"detail": "Item Removed Succesfully."}, status=status.HTTP_204_NO_CONTENT)"""
    
'''class PostDetail(APIView):
    """ getting detail of the post and edit plus removing it. """
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    
    def get(self, request, id):
        """retriving the post data"""
        post = get_object_or_404(Post, pk=id, status=True)
        serializer = self.serializer_class(post)
        return Response(serializer.data) 
    
    def put(self, request, id):
        """ editing the post data """
        post = get_object_or_404(Post, pk=id, status=True)
        serializer = PostSerializer(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, id):
        """ Deleting the post object """
        post = get_object_or_404(Post, pk=id, status=True)
        post.delete()
        return Response({"detail": "Item Removed Succesfully."}, status=status.HTTP_204_NO_CONTENT)
'''

'''class PostDetail(RetrieveUpdateDestroyAPIView):
    """ getting detail of the post and edit plus removing it. """
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)'''


class PostModelViewSet(viewsets.ModelViewSet):
    """ getting a list of posts & creating a new post """
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = {'category':["exact", "in"], 'author':["exact"],'status':["exact"]}  
    search_fields = ['title', 'content']
    ordering_fields = ['published_date']
    pagination_class = DefaultPagination


class CategoryModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

        
