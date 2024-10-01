from django.contrib import admin
from .models import Student, BlogPost, Author, AuthorProfile,CommentPost,Contact
# Register your models here.

admin.site.register(Student)
admin.site.register(BlogPost)
admin.site.register(Author)
admin.site.register(AuthorProfile)
admin.site.register(CommentPost)
admin.site.register(Contact)

