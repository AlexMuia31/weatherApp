
from django.conf.urls import url
from django.contrib import admin
from app import views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('',views.home, name='home')
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
