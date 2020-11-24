from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("", views.home, name="Home"),
    path("detail/<int:id>/", views.detail, name="Detail"),
    path("detail_info/<int:id>/", views.detail_info, name="detail_info"),
    path("upload_info/", views.upload_info, name="upload_info"),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
