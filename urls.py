from django.contrib import admin
from django.urls import path
from home.views import home, delete_student, edit_student
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("admin/", admin.site.urls),

    path("", home, name="home"),

    path("delete/<int:id>/", delete_student, name="delete_student"),

    path("edit/<int:id>/", edit_student, name="edit_student"),

    
]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )