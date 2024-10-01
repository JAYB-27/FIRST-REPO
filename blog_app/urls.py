from django.urls import path
from .views import home_page, about_page, contact_page, blog_detail_page,post_page,author_profile_page, register_new_author, addblogpost

urlpatterns= [
    path('', home_page, name='home-page'),
    path('about/', about_page, name='about'),
    path('contact/', contact_page, name='contact'),
    path('blog-post/<int:post_id>/', blog_detail_page, name="blog-post"),
    path('post/', post_page, name='post'),                                                      
    path('profile/<int:author_id>/', author_profile_page, name="profile"),
    path('createn-author/', register_new_author, name='new_author'),
    path('create-post/<int:author_id>/', addblogpost, name="new_post"),
]