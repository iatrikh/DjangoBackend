from rest_framework.serializers import ModelSerializer, IntegerField, DecimalField, CharField
from django.contrib.auth.models import User

from store.models import Book
from store.models import UserBookRelation

class BookReaderSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')

class BookSerializer(ModelSerializer):
    annotated_likes= IntegerField(read_only=True)
    rating = DecimalField(max_digits=3, decimal_places=2, read_only=True)
    owner_name = CharField(source='owner.username', default='No owner', read_only=True)
    readers = BookReaderSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = ('id', 'name', 'price', 'author_name', 'annotated_likes', 'rating', 'owner_name', 'readers')
    

class UserBookRelationSerializer(ModelSerializer):
    class Meta:
        model = UserBookRelation
        fields = ('book', 'like', 'in_bookmarks', 'rate')