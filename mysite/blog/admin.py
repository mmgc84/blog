from django.contrib import admin
from hvad.admin import TranslatableAdmin
from blog.models import Post, Comment, Autor


# Register your models here.
class CommentInline(admin.StackedInline):
    model = Comment
    extra = 0


class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Posts', {'fields': [
            'post_author', 'post_title', 'post_text', 'pub_date']}),
    ]
    inlines = [CommentInline]
    list_display = ('post_author', 'post_title', 'post_text', 'pub_date')
    list_filter = ['post_author']
    search_fields = ['post_title', 'post_author']


class AutorAdmin(TranslatableAdmin):
    list_display = ['name']


admin.site.register(Post, PostAdmin)
admin.site.register(Autor, AutorAdmin)
