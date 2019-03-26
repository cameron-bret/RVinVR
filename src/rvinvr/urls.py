from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from posts.views import (
    index, about, blog, post, search, 
    post_create, post_update, post_delete)
from marketing.views import email_list_signup

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('about/', about),
    path('blog/', blog, name='post-list'),
    path('search/', search, name='search'),
    path('subscribe/', email_list_signup, name='subscribe'),
    path('create/', post_create, name='post-create'),
    path('post/<id>/', post, name='post-detail'),
    path('post/<id>/update/', post_update, name='post-update'),
    path('post/<id>/delete/', post_delete, name='post-delete'),
    path('tinymce/', include('tinymce.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)