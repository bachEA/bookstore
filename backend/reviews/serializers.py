# Serializers class has two important purpose

# First it converts data into JSON
# Second it specify which fields (in models) to include or exclude


from rest_framework import serializers
from .models import Review


class ReviewSerializer(serializers.ModelSerializer):


    # to customize which fields to include or exclude
    class Meta:

        fields = ('id', 'author', 'title', 'body', 'created_at')
        model = Review
