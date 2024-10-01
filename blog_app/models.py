from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.dispatch import receiver



    # Create your models here.
class Student(models.Model):
        names=models.CharField(max_length=200)
        age=models.PositiveIntegerField(default=0)
        email=models.EmailField(max_length=200)
        address=models.TextField()
    


        def __str__(self) -> str:
            return self.names
        
   

class Contact(models.Model):
      names=models.CharField(max_length=200)
      email=models.EmailField(max_length=50)
      phone=models.PositiveIntegerField()
      message=models.CharField(max_length=1000)


      def __str__(self) -> str:
            return self.names



class Author(models.Model):
      names=models.CharField(max_length=200)
      email=models.EmailField(max_length=255)

      def __str__(self) -> str:
            return self.names

   

class AuthorProfile(models.Model):
      author=models.OneToOneField(Author, on_delete=models.CASCADE)
      bio=models.TextField(null=True, blank=True)
      birth_date=models.DateField(null=True, blank=True)
      country=models.CharField(max_length=50, null=True, blank=True)
      profile_img=models.ImageField(upload_to="profile/", default="profile/default.png")

      def __str__(self):
            return self.author.names
           



class   BlogPost(models.Model):
      title=models.CharField(max_length=300)
      description=models.TextField()
      content=RichTextField()
      published_date=models.DateField(auto_now_add=True)
      post_banner=models.ImageField(upload_to="blogpost/")
      owner=models.ForeignKey(Author, on_delete=models.CASCADE, default=1)

      def __str__(self) -> str:
            return self.title
      

class CommentPost(models.Model):
      name=models.CharField(max_length=200)
      email=models.EmailField(max_length=200)
      comment=models.TextField(max_length=400)
      created_at=models.DateTimeField(auto_now_add=True)
      post= models.ForeignKey(BlogPost, on_delete=models.CASCADE)

      def __str__(self) -> str:
            # return f"{self.name}-comment"
            return self.comment
      