from django.urls import path

from .views import CategoryViewSet, PostRetrieveUpdateDestroyAPIView, CommentRetrieveUpdateDestroyAPIView, \
    CommentListCreateAPIView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='categories')
urlpatterns = router.urls

urlpatterns += [
    path('posts/<int:pk>/', PostRetrieveUpdateDestroyAPIView.as_view()),
    path('comment/<int:pk>/', CommentRetrieveUpdateDestroyAPIView.as_view()),
    path('posts/<int:pk>/comments/', CommentListCreateAPIView.as_view())
]
