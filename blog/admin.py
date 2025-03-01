from django.contrib import admin
from .models import Post
# from .models import Author

# class AuthorAdmin(admin.ModelAdmin):
#     pass
# admin.site.register(Author, AuthorAdmin)

admin.site.register(Post)