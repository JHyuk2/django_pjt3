from django.contrib import admin
from .models import Review, Comment
# Register your models here.

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'created_at', 'updated_at', 'creator')

class CommentAdmin(admin.ModelAdmin):
    list_dispaly = ('id','review_id', 'creator')

admin.site.register(Review, ReviewAdmin)
admin.site.register(Comment, CommentAdmin)