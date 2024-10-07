from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from .filters import ProductFilter
from .models import Category, Product, Review
from .serializers import (CategorySerializer, ProductSerializer, ReviewSerializer, RegisterSerializer, LoginSerializer,
                          LogoutSerializer)
from .permissions import IsAdminOrReadOnly
from .pagination import StandPagination


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminOrReadOnly]
    #pagination_class = StandPagination

    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]
    #pagination_class = StandPagination


class RegisterViewsSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]


class LoginViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]


class LogoutViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = LogoutSerializer
    permission_classes = [IsAuthenticated]




