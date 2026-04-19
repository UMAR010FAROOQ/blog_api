from rest_framework.routers import DefaultRouter
from django.urls import path, include
from blog.views import PostViewSet, CategoryViewSet, CommentViewSet, RegisterView
from rest_framework.authtoken.views import obtain_auth_token


router = DefaultRouter()

router.register(r'posts', PostViewSet, basename='post')
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'comments', CommentViewSet, basename='comment')


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('', include(router.urls)),
    path('login/', obtain_auth_token),
    path('register/', RegisterView.as_view(), name='register'),


    path('jwt/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('jwt/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

