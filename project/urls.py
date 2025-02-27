from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static  # استيراد الدالة static
<<<<<<< HEAD

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('network.urls')),  # استبدل 'network' باسم تطبيقك إذا كان مختلفًا
]

=======
from network import views

urlpatterns = [
      path('', views.splash, name='splash'),
      path('', include('network.urls')),  # تغيير الصفحة الرئيسية إلى splash
      path('index/', views.index, name='index'),
      path('users/', views.users, name='users'),
        # جعل الصفحة الرئيسية في مسار مختلف
]


>>>>>>> 2aa59cd686b20bd9b1ab5b8b7dda1a956fc18380
# إضافة مسار لخدمة الوسائط (Media)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)