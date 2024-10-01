from django import forms
from ckeditor.fields import RichTextField
from ckeditor.widgets import CKEditorWidget
from .models import CommentPost


class AddBlogPostForm(forms.Form):
    title=forms.CharField(max_length=250,widget=forms.TextInput(attrs={"class":'form'}))
    description=forms.CharField(widget=forms.Textarea(attrs={"class": 'form-control'}))
    content=forms.CharField(widget=CKEditorWidget (attrs={"class": 'form-control'}))
    post_banner=forms.ImageField()



class AddCommentForm(forms.ModelForm):
    class Meta:
        model=CommentPost
        fields=['name', 'email', 'comment']
        widgets={
            'names':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':"form-control"}),
            'comment':forms.Textarea(attrs={'class':"form-control"}),
        }

