from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from library.models import Book
from library.serializers import BookSerializer
from rest_framework.decorators import api_view, permission_classes
from library.serializers import CategorySerializer
from library.models import Category

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Welcome in Library!'}
        return Response(content)


@api_view(['GET', 'POST', 'DELETE'])
@permission_classes([IsAuthenticated])
def book_list(request):
    if request.method == 'GET':
        books = Book.objects.all().order_by('id')

        title = request.query_params.get('title', None)
        if title is not None:
            books = books.filter(title__icontains=title)

        books_serializer = BookSerializer(books, many=True)
        return JsonResponse(books_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        book_data = JSONParser().parse(request)
        book_serializer = BookSerializer(data=book_data)
        if book_serializer.is_valid():
            book_serializer.save()
            return JsonResponse(book_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(book_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Book.objects.all().delete()
        return JsonResponse({'message': '{} Books were deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def book_detail(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return JsonResponse({'message': 'The book does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        book_serializer = BookSerializer(book)
        return JsonResponse(book_serializer.data)

    elif request.method == 'PUT':
        book_data = JSONParser().parse(request)
        book_serializer = BookSerializer(book, data=book_data)
        if book_serializer.is_valid():
            book_serializer.save()
            return JsonResponse(book_serializer.data)
        return JsonResponse(book_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        book.delete()
        return JsonResponse({'message': 'Book was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def book_list_available(request):
    books = Book.objects.filter(available=True).order_by('id')

    if request.method == 'GET':
        books_serializer = BookSerializer(books, many=True)
        return JsonResponse(books_serializer.data, safe=False)


@api_view(['GET'])
def book_list_not_available(request):
    books = Book.objects.filter(available=False).order_by('id')

    if request.method == 'GET':
        books_serializer = BookSerializer(books, many=True)
        return JsonResponse(books_serializer.data, safe=False)


@api_view(['GET'])
def book_category(request):
    name = Category.objects

    if request.method == 'GET':
        category_serializer = CategorySerializer(name, many=True)
        return JsonResponse(category_serializer.data, safe=False)


@api_view(['GET', 'POST', 'DELETE'])
def category_list(request):
    if request.method == 'GET':
        category = Category.objects.all().order_by('id')

        categories = request.query_params.get('category', None)
        if categories is not None:
            category = category.filter(category__icontains=categories)

        category_serializer = CategorySerializer(category, many=True)
        return JsonResponse(category_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        category_data = JSONParser().parse(request)
        category_serializer = CategorySerializer(data=category_data)
        if category_serializer.is_valid():
            category_serializer.save()
            return JsonResponse(category_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(category_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Category.objects.all().delete()
        return JsonResponse({'message': '{} Categories were deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def category_detail(request, pk):
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return JsonResponse({'message': 'The category does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        category_serializer = CategorySerializer(category)
        return JsonResponse(category_serializer.data)

    elif request.method == 'PUT':
        category_data = JSONParser().parse(request)
        category_serializer = CategorySerializer(category, data=category_data)
        if category_serializer.is_valid():
            category_serializer.save()
            return JsonResponse(category_serializer.data)
        return JsonResponse(category_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        category.delete()
        return JsonResponse({'message': 'Category was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


# Create your views here.
