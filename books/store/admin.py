from django.contrib import admin
from django.contrib.admin import ModelAdmin

from store.models import Book
from store.models import UserBookRelation

# Register your models here.
@admin.register(Book)
class BookAdmin(ModelAdmin):
    pass


@admin.register(UserBookRelation)
class UserBookRelationAdmin(ModelAdmin):
    pass