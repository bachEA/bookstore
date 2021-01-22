from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Review
from .serializers import ReviewSerializer
from .permissions import IsAuthorOrReadOnly

# Create your views here.

class ReviewList(generics.ListCreateAPIView):

    # update authenticate at view level
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
