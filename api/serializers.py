from rest_framework import serializers
from base.models import Book, Client

class BookSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='surname'
    )
    author_name = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        source='author',
        slug_field='name'
    )
    category = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='category'
    )
    release_place = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        source='release',
        slug_field='release_place'
    )
    release_year = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        source='release',
        slug_field='release_year'
    )
    class Meta:
        model = Book
        fields = ['id', 'author', 'title', 'image', 'category', 'release_place', 'release_year', 'status', 'author_name']



class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'
