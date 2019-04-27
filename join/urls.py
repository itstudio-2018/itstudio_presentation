from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^api/apply/', views.apply),
    url(r'^confirm/', views.confirm),
]
