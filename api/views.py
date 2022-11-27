from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Book, Client, Hire, Author, Category, Release, Status
from rest_framework.parsers import JSONParser
from rest_framework.decorators import parser_classes
from .serializers import BookSerializer, ClientSerializer, HireSerializer

@api_view(['GET'])
def getData(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@parser_classes([JSONParser])
def createHire(request, format=None):
    serializer = HireSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response({'received data': request.data})

@api_view(['POST'])
@parser_classes([JSONParser])
def addBook(request, format=None):
    author = Author.objects.filter(surname=request.data['author']).first()
    category = Category.objects.filter(category=request.data['category']).first()
    release = Release.objects.filter(release_place=request.data['release_place']).first()
    status = Status().save()
    instance = Book(author=author, title=request.data['title'], category=category, release=release, image=request.data['image'], status=status)
    instance.save()
    serializer = BookSerializer(instance)
    return Response({'received data': serializer.data})

@api_view(['GET'])
def getClients(request):
    clients = Client.objects.all()
    serializer = ClientSerializer(clients, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def createUser(request):
    serializer = ClientSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def getAllHires(request):
    hires = Hire.objects.all()
    serializer = HireSerializer(hires, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getBookByString(request, book_name):
    book = Book.objects.get(title=book_name)
    serializer = BookSerializer(book, many=False)
    return Response(serializer.data)

@api_view(['GET'])
@parser_classes([JSONParser])
def getClientByLogin(request, login, format=None):
    client = Client.objects.get(login=login)
    serializer = ClientSerializer(client, many=False)
    return Response(serializer.data)




