from copy import deepcopy

from django.shortcuts import render
from rest_framework import viewsets, generics, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Category, Post, Comment
from .permissions import CategoryPermission, IsOwnerOfObjectOrRead
from .serializers import CategorySerializer, PostSerializer, CommentSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (CategoryPermission, )


    @action(detail=True, methods=["post", "get"], url_path="posts") 
    def posts_for_category(self, request, pk): 
        if request.method == "GET":
            posts = Post.objects.filter(category_id=pk)  
            post_serializer = PostSerializer(posts, many=True)
            return Response(post_serializer.data)
        else:
            data = deepcopy(request.data)
            category = self.get_object()
            post_serializer = PostSerializer(data=data, context={
                'request': request})  

            if post_serializer.is_valid():
                post = Post(**post_serializer.validated_data, category=category)
                post.save() 
                return Response(post_serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(post_serializer.errors,
                                status=status.HTTP_400_BAD_REQUEST)


class PostRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsOwnerOfObjectOrRead, )
    

class CommentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsOwnerOfObjectOrRead,)



class CommentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        post_pk = self.kwargs.get('pk')  
        queryset = super().get_queryset().filter(post_id = post_pk) 
        return queryset


    def perform_create(self, serializer):
        serializer.save(post = self.kwargs.get('pk'))


