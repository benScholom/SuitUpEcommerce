from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.home, name = 'home'),
    url(r'^about/$', views.about, name="about"),
    url(r'^contact/$', views.contact, name="contact")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)