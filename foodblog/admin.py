from django.contrib import admin
from .models import Recipe, Category, Comment

# Category Admin
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

# Comment Admin
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('recipe', 'author', 'content', 'created_at')
    list_filter = ('created_at', 'author')
    search_fields = ('content', 'author__username')


# Recipe Admin
@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'created_at', 'upvotes', 'downvotes')
    list_filter = ('created_at', 'category', 'author')
    search_fields = ('title', 'description', 'ingredients', 'author__username')
    ordering = ('-created_at',)