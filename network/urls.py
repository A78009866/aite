from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
<<<<<<< HEAD
=======
from django.contrib.auth import views as auth_views
>>>>>>> 2aa59cd686b20bd9b1ab5b8b7dda1a956fc18380
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_post/', views.add_post, name='add_post'),
    path('delete_post/<int:post_id>/', views.delete_post, name='delete_post'),
    path('like_post/<int:post_id>/', views.like_post, name='like_post'),
    path('add_comment/<int:post_id>/', views.add_comment, name='add_comment'),
    path('delete_comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),
    path('edit_comment/<int:comment_id>/', views.edit_comment, name='edit_comment'),
    path('login/', views.login_view, name='login'),
<<<<<<< HEAD
    path('logout/', views.logout_view, name='logout'),
=======
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  
>>>>>>> 2aa59cd686b20bd9b1ab5b8b7dda1a956fc18380
    path('register/', views.register, name='register'),
    path('users/', views.users_list, name='users'),
    path('send_friend_request/<int:user_id>/', views.send_friend_request, name='send_friend_request'),
    path('accept_friend_request/<int:request_id>/', views.accept_friend_request, name='accept_friend_request'),
    path('reject_friend_request/<int:request_id>/', views.reject_friend_request, name='reject_friend_request'),
    path('friend_requests/', views.friend_requests, name='friend_requests'),
    path('send_message/<int:user_id>/', views.send_message, name='send_message'),
    path('messages/<int:user_id>/', views.messages, name='messages'),
    path('message_list/', views.message_list, name='message_list'),
<<<<<<< HEAD
    path('profile/', views.profile, name='profile'),  # جديد
    path('update_profile/', views.update_profile, name='update_profile'),  # جديد
]

# إضافة مسار لخدمة الوسائط (Media)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
=======
    path('profile/<str:username>/', views.profile, name='profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('splash/', views.splash, name='splash'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
>>>>>>> 2aa59cd686b20bd9b1ab5b8b7dda1a956fc18380
