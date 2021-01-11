from rest_framework import serializers
from library.models import Book
from library.models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id',
                  'title',
                  'author',
                  'description',
                  'category',
                  'available')
