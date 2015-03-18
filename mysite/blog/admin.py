from django.contrib import admin

from blog.models import Post, Comment


# Register your models here.
class CommentInline(admin.StackedInline):
    model = Comment
    extra = 0


class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Posts', {'fields': ['post_title', 'post_text', 'pub_date']}),
    ]
    inlines = [CommentInline]

admin.site.register(Post, PostAdmin)
