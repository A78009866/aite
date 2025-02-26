from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static  # استيراد الدالة static
from network import views

urlpatterns = [
      path('', views.splash, name='splash'),
      path('', include('network.urls')),  # تغيير الصفحة الرئيسية إلى splash
      path('index/', views.index, name='index'),
        # جعل الصفحة الرئيسية في مسار مختلف
]
from django.urls import path
from network import views  # تأكد من أنك تستورد views بشكل صحيح

urlpatterns = [
    path('users/', views.users, name='users'),  # تأكد من أن لديك هذا السطر
]


# إضافة مسار لخدمة الوسائط (Media)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)