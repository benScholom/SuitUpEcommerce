from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^$', views.home, name = 'home'),
    url(r'^about/$', views.about, name="about"),
    url(r'^contact/$', views.contact, name="contact"),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', login, name='login'),
    url(r'^userlogout/$', views.user_logout, name='userlogout'),
    #url(r'^logout/$', logout, name='logout'),
    url(r'^suit/$', views.suits_view, name='suits'),
    url(r'^shirt/$', views.shirts_view, name='shirts'),
    url(r'^shoes/$', views.shoes_view, name='shoes'),
    url(r'^tie/$', views.ties_view, name='ties'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)